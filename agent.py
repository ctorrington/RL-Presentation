"""RL Agent to interact with a given environment."""

from grid_world import GridWorld

class Agent:
    """RL Agent."""

    def __init__(self) -> None:
        self.grid_world = GridWorld()

        self.policy = "random"
        print(self.grid_world._get_available_actions((0, 0)))
