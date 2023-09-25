"""
Demonstration project for a finite Markov Decision Process with a Grid World.
"""

from constants import Constants

ACTIONS = Constants.ACTIONS

class GridWorld:
    """Grid World Environment."""

    def __init__(self) -> None:
        """Initialse the Grid World Environment."""

        # State space properties.
        self.number_of_rows = 5
        self.number_of_columns = 5
        self.terminal_states = [(self.number_of_rows - 1,
                                 self.number_of_columns - 1)]

        self.state_space = {}

        # State attributes setup.
        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                # Properties of each state.
                state = (row, column)
                self.state_space[state] = {
                    "actions": [],
                    "return": 0,
                    "reward": 0
                }

                # Actions of each state.
                for action in ACTIONS.as_tuple():
                    match action:
                        case ACTIONS.UP:
                            # Check top border.
                            if row == self.number_of_rows - 1:
                                continue

                        case ACTIONS.DOWN:
                            # Check bottom border.
                            if row == 0:
                                continue

                        case ACTIONS.LEFT:
                            # Check left border.
                            if column == 0:
                                continue

                        case ACTIONS.RIGHT:
                            # Check right border.
                            if column == self.number_of_columns - 1:
                                continue

                    self.state_space[state]["actions"].append(action.name)

        # Terminal states rewards.
        for state in self.terminal_states:
            self.state_space[state]["reward"] = 1
            
        print("we gucci")

    def print_state_space(self) -> None:
        """Print the state space."""

        for state in self.state_space:
            print(f"{state}: {self.state_space[state]}")
