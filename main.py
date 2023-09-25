from grid_world import GridWorld
from agent import Agent

if __name__ == "__main__":
    # grid_world = GridWorld()
    # grid_world.print_state_space()

    agent = Agent()
    # print(grid_world._get_available_actions((1, 2)))
    # print(agent._get_action_probability_distribution((1, 2)))
    agent.determine_state_value_over_state_space()
    agent.grid_world.print_state_space()
    