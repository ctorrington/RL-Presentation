"""Plot data."""

from agent import Agent
from grid_world import GridWorld
from constants import Constants

import matplotlib.pyplot as plt
import matplotlib.animation as mpla
import numpy as np

ACTIONS = Constants.ACTIONS
State = Constants.State

class Plotter:
    def __init__(self) -> None:
        pass

    def create_z_axis_data(self, data: GridWorld, ax) -> list[list[int]]:
        """Return the data for the imshow function in the correct format."""

        # print(data.print_state_space())

        data_matrix = []

        for x in range(data.get_number_of_rows()):
            row = []
            for y in range(data.get_number_of_columns()):
                state = (x, y)
                # Check if the state is an obstacle.
                if state in data._get_obstacles():
                    # Append a for for no returns if it is an obstacle.
                    row.append(0)
                else:
                    # Otherwise append state return value.
                    row.append(data.state_space[state]["return"])
                    
                # Add the annotations for action directions.
                self.annotate(state, data, ax)
                
            data_matrix.append(row)

        return data_matrix
    
    def annotate(self, state: State,
                 environment: GridWorld,
                 ax) -> None:
        """Add annotations to the plot."""
        
        arrow_start_position = (state[0], state[1])
        arrow_directions = list[ACTIONS]
        
        if len(environment._get_available_actions(state)) > 0:
            print(state)
            print(environment._get_available_actions(state))
            arrow_directions = environment._get_available_actions(state)
        else:
            # No available actions for the state.
            return
        
        for direction in arrow_directions:
            match direction:
                case ACTIONS.UP:
                    xytext = (state[0], state[1] + 1)

                case ACTIONS.DOWN:
                    xytext = (state[0], state[1] - 1)

                case ACTIONS.LEFT:
                    xytext = (state[0] - 1, state[1])

                case ACTIONS.RIGHT:
                    xytext = (state[0] + 1, state[1])                

                case _:
                    print("I should I written a proper error message.")
                    return
                
        ax.annotate("",
                    xy = arrow_start_position,
                    xytext = xytext,
                    arrowprops = dict(arrowstyle = "<-",
                                    color = "orange"))
        
    
    def plot_animation(self, agent: Agent) -> None:

        history: list[GridWorld] = agent.history

        fig, ax = plt.subplots()
        ax.set_xlim(0, agent.grid_world.get_number_of_columns())
        ax.set_ylim(0, agent.grid_world.get_number_of_rows())
        
        plot_data = ax.imshow(self.create_z_axis_data(history[0], ax))

        def animate(i):
            # Plot the state space.
            plot_data.set_data(self.create_z_axis_data(history[i], ax))
            
            # Annotate the arrows to show direction for each state.
            # annotate(i)

        anim = mpla.FuncAnimation(
            plt.gcf(),
            animate,
            frames = len(history),
            interval = 100,
            repeat = True
        )
        plt.show()
