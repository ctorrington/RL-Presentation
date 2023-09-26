"""Plot data."""

from agent import Agent
from constants import Constants

import matplotlib.pyplot as plt
import matplotlib.animation as mpla
import numpy as np

ACTIONS = Constants.ACTIONS

class Plotter:
    def __init__(self) -> None:
        pass

    def create_z_axis_data(self, data) -> list[list[int]]:
        """Return the data for the imshow function in the correct format."""

        # print(data.print_state_space())

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
    
    def plot_animation(self, agent: Agent) -> None:

        data = agent.history

        fig, ax = plt.subplots()
        plot_data = ax.imshow(self.create_z_axis_data(data[0]))

        def annotate(i):
            # For every state in the environment.
            for state in data[i].state_space:
                arrow_direction = (state[0], state[1])
                # Catch list index out of range error for no avialable actions.
                # Check that the list is not empty.
                if len(data[i]._get_available_actions(state)) > 0:
                    action_direction = data[i]._get_available_actions(state)[0]
                else:
                    # If the list is empty, don't draw an arrow.
                    continue

                match action_direction:
                    case ACTIONS.UP:
                        xytext = (state[0] - 1, state[1])

                    case ACTIONS.DOWN:
                        xytext = (state[0] + 1, state[1])

                    case ACTIONS.LEFT:
                        xytext = (state[0], state[1] - 1)

                    case ACTIONS.RIGHT:
                        xytext = (state[0], state[1] + 1)                

                    case _:
                        xytext = (state[0]. state[1])

                ax.annotate("",
                            xy = arrow_direction,
                            xytext = xytext,
                            arrowprops = dict(arrowstyle = "->",
                                            color = "black"))

        def animate(i):
            plot_data.set_data(self.create_z_axis_data(data[i]))
            # annotate(i)

        anim = mpla.FuncAnimation(
            plt.gcf(),
            animate,
            frames = len(data),
            interval = 5,
            repeat = True
        )
        plt.show()
