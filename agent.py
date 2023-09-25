"""RL Agent to interact with a given environment."""

from grid_world import GridWorld
from constants import Constants

ACTIONS = Constants.ACTIONS

class Agent:
    """RL Agent."""

    def __init__(self) -> None:
        self.grid_world = GridWorld()

        self.policy = "random"

    def _get_action_probability_distribution(self, state: tuple[int, int]) -> dict[ACTIONS,
                                                                      int]:
        """Return the probability distribution of taken each action
        available to the given state."""

        action_probability_distribution = {}

        # Random policy.
        if self.policy == "random":
            # The agent follows a random policy.
            # All actions are chosen equally randomly.
            available_actions = self.grid_world._get_available_actions(state)
            action_probability = 1 / len(available_actions)
            for action in available_actions:
                action_probability_distribution[action] = 1 / len(available_actions)

        # Other policies. (future work)
        else:
            pass

        return action_probability_distribution
