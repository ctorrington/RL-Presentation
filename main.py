from agent import Agent
from plotter import Plotter

if __name__ == "__main__":
    agent = Agent()

    agent.determine_state_value_over_state_space()
    agent.grid_world.print_state_space()
    agent.get_environment()

    plotter = Plotter(agent.grid_world.get_number_of_rows(),
                      agent.grid_world.get_number_of_columns(),
                      agent.grid_world.get_state_space())
    plotter.plot_animation(agent.history)
    