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
                    if self._is_valid_action(action, state):
                        self.state_space[state]["actions"].append(action)

        # Terminal states rewards.
        for state in self.terminal_states:
            self.state_space[state]["reward"] = 1
            
        print("we gucci")

    def _is_valid_action(self,
                         action: ACTIONS,
                         state: tuple[int, int]) -> bool:
        """Return whether a given action is valid in a given state."""

        match action:
            case ACTIONS.UP:
                # Check top border.
                if state[0] == self.number_of_rows - 1:
                    return False

            case ACTIONS.DOWN:
                # Check bottom border.
                if state[0] == 0:
                    return False

            case ACTIONS.LEFT:
                # Check left border.
                if state[1] == 0:
                    return False

            case ACTIONS.RIGHT:
                # Check right border.
                if state[1] == self.number_of_columns - 1:
                    return False

        return True

    def _get_available_actions(self, state: tuple[int, int]) -> list[ACTIONS]:
        """Return the available actions for the given state."""
        return self.state_space[state]["actions"]
    
    def _get_state_transition_probability(self,
                                          state: tuple[int, int],
                                          action: ACTIONS) -> float | int:
        """
        Return the probability of transitioning to the next state with the
        given state & action.
        """

        # TODO add the 'wind' affect here later.        

        return 1
    
    def _get_next_state(self,
                        state: tuple[int, int],
                        action: ACTIONS) -> tuple[int, int]:
        """
        Return the next state from the given state & action IRRESPECTIVE of
        the state transition probability.
        """

        match action:
            case ACTIONS.UP:
                next_state = (state[0] + 1, state[1])

            case ACTIONS.DOWN:
                next_state = (state[0] - 1, state[1])

            case ACTIONS.LEFT:
                next_state = (state[0], state[1] - 1)

            case ACTIONS.RIGHT:
                next_state = (state[0], state[1] + 1)

        return next_state

    def print_state_space(self) -> None:
        """Print the state space."""

        for state in self.state_space:
            print(f"{state}: {self.state_space[state]}")
