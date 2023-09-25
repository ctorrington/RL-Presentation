"""RL Agent to interact with a given environment."""

from grid_world import GridWorld
from constants import Constants

ACTIONS = Constants.ACTIONS

class Agent:
    """RL Agent."""

    def __init__(self) -> None:
        self.grid_world = GridWorld()
        self.policy = "random"
        self.gamma = 1

    def _get_action_probability_distribution(self, state: tuple[int, int]) -> dict[ACTIONS, float | int]:
        """
        Return the probability distribution of taken each action
        available to the given state.
        """

        action_probability_distribution = {}

        # Random policy.
        if self.policy == "random":
            # The agent follows a random policy.
            # All actions are chosen equally randomly.
            available_actions = self.grid_world._get_available_actions(state)
            action_probability = 1 / len(available_actions)
            for action in available_actions:
                action_probability_distribution[action] = action_probability

        # Other policies. (future work)
        else:
            pass

        return action_probability_distribution
    
    def _determine_state_value(self, state: tuple[int, int]) -> float | int:
        """Return the estimated state value for the given state."""

        state_value = self.grid_world._get_state_return(state)

        action_probability_distribution = self._get_action_probability_distribution(state)

        for action in action_probability_distribution:
            action_probability = action_probability_distribution[action]
            next_state = self.grid_world._get_next_state(state, action)
            reward = self.grid_world._get_state_reward(next_state)

            state_value += (action_probability * self.grid_world._get_state_transition_probability(state, action) * (reward + (self.gamma * self.grid_world._get_state_return(next_state))))

        return state_value

    def determine_state_value_over_state_space(self) -> None:
        """
        Determine the state values of all states within the given state space.
        """

        for state in self.grid_world.state_space:
            self.grid_world._set_state_return(state,
                                              self._determine_state_value(state))
            
        # Reset the return for the terminal states - should should not have any.
        # Doing it like this, rather than with an if statement, for performance.
        for state in self.grid_world._get_terminal_states():
            self.grid_world._set_state_return(state, 0)
