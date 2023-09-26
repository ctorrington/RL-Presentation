"""Plot data."""

import matplotlib.pyplot as plt
import matplotlib.animation as mpla
import numpy as np

class Plotter:
    def __init__(self) -> None:
        pass

    def create_z_axis_data(self, data) -> list[list[int]]:
        """Return the data for the imshow function in the correct format."""

        print(data.print_state_space())

        data_matrix = []

        for x in range(data.get_number_of_rows()):
            row = []
            for y in range(data.get_number_of_columns()):
                state = (x, y)
                # Check if the state is an obstacle.
                if state in data._get_obstacles():
                    # Append a for for no returns if it is an obstacle.
                    row.append(0)
                else:
                    # Otherwise append state return value.
                    row.append(data.state_space[state]["return"])
            data_matrix.append(row)

        return data_matrix
    
    def plot_animation(self, data) -> None:

        plot_data = plt.imshow(self.create_z_axis_data(data[0]))
        # plot_data = plt.imshow(self.create_z_axis_data(data[len(data) - 1]))

        def animate(i):
            plot_data.set_data(self.create_z_axis_data(data[i]))

        anim = mpla.FuncAnimation(
            plt.gcf(),
            animate,
            frames = len(data),
            interval = 50,
            repeat = False
        )
        plt.show()
