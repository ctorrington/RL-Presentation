"""Plot data."""

import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self, x, y , z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def plot_data(self) -> None:
        """Plot the data given."""

        fig, ax = plt.subplots()
        im = ax.imshow(self.create_z_axis_data())
        plt.show()

    def create_z_axis_data(self) -> list[list[int]]:
        """Return the data for the imshow function in the correct format."""

        data = []

        for x in range(self.x):
            row = []
            for y in range(self.y):
                state = (x, y)
                row.append(self.z[state]["return"])
            data.append(row)

        return data
