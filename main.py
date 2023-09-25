"""
Demonstration project for a finite Markov Decision Process with a Grid World.
"""

class GridWorld:
    """Grid World Environment."""

    def __init__(self) -> None:
        """Initialse the Grid World Environment."""

        # State space values.
        self.number_of_rows = 5
        self.number_of_columns = 5

        self.state_space = {}

        # State attributes setup.
        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                # Properties of each state.
                state = (row, column)
                self.state_space[state] = {
                    "actions": {},
                    "return": 0,
                    "reward": 0
                }
                