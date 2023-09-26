from agent import Agent
from plotter import Plotter

if __name__ == "__main__":
    agent = Agent()

    agent.determine_state_value_over_state_space()
    agent.grid_world.print_state_space()
    agent.get_environment()

    plotter = Plotter()
    plotter.plot_animation(agent)
