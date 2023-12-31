"""RL Agent to interact with a given environment."""

from grid_world import GridWorld
from constants import Constants

import copy

ACTIONS = Constants.ACTIONS
State = Constants.State

class Agent:
    """RL Agent."""

    def __init__(self) -> None:
        self.grid_world = GridWorld()
        self.policy = "random"  # Policy followed by agent.
        self.gamma = 0.9999  # Discounting parameter.
        self.theta = 0.001  # Accuracy parameter.
        self.history: list[GridWorld] = []  # History of environment updates.

    def _get_action_probability_distribution(self, state: State) -> dict[ACTIONS, float | int]:
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
            # Prevent division by zero error.
            if len(available_actions) > 0:
                action_probability = 1 / len(available_actions)
            else:
                action_probability = 0
            for action in available_actions:
                action_probability_distribution[action] = action_probability

        # Other policies. (future work)
        else:
            pass

        return action_probability_distribution
    
    def get_environment(self) -> GridWorld:
        """Return the environment with values determined by the agent."""

        return self.grid_world
    
    def _determine_state_return(self, state: State) -> float | int:
        """Return the estimated state value for the given state."""

        state_value = self.grid_world._get_state_return(state)
        possible_actions = self.grid_world._get_available_actions(state)
        action_probability_distribution = self._get_action_probability_distribution(state)

        expected_return = 0

        # For every action in the state...
        for action in possible_actions:
            action_probability = action_probability_distribution[action]
            possible_next_states = self.grid_world._get_next_states(state, action)

            # For every possible next state from the currect action...
            for next_state in possible_next_states:
                next_state_probability = self.grid_world._get_state_transition_probability(state, action, next_state)
                next_state_reward = self.grid_world._get_state_reward(next_state)
                next_state_return = self.grid_world._get_state_return(next_state)

                action_return = next_state_probability * (next_state_reward + (self.gamma * next_state_return))
                expected_return += action_probability * action_return

        state_value = expected_return

        return state_value

    def determine_state_value_over_state_space(self) -> None:
        """
        Determine the state values of all states within the given state space.
        """

        terminal_states = self.grid_world._get_terminal_states()

        # Update the state values until a desired accuracy is reached.
        while True:
            delta = 0 # 💀

            # Update the value (expected return) for each state.
            for state in self.grid_world.state_space:
                if state not in terminal_states:
                    previous_state_return = self.grid_world._get_state_return(state)
                    self.grid_world._set_state_return(state, self._determine_state_return(state))
                    state_return_difference = abs(previous_state_return - self.grid_world._get_state_return(state))
                    delta = max(delta, state_return_difference)

            # Update the history for plotting.
            self.history.append(copy.deepcopy(self.grid_world))
                
            # Check for convergence after updating all the states.
            if delta < self.theta:
                break
