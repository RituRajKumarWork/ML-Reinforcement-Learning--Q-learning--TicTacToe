# agent.py
import numpy as np
import random
from collections import defaultdict

class QLearningAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, decay_rate=0.995):
        self.q_table = defaultdict(lambda: np.zeros((3, 3)))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.decay_rate = decay_rate

    def choose_action(self, state, available_actions):
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(available_actions)
        q_values = [self.q_table[tuple(map(tuple, state))][action] for action in available_actions]
        return available_actions[np.argmax(q_values)]

    def update_q_table(self, state, action, reward, next_state):
        current_q = self.q_table[tuple(map(tuple, state))][action]
        max_future_q = np.max([self.q_table[tuple(map(tuple, next_state))][a] for a in available_actions(next_state)], initial=0)
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)
        self.q_table[tuple(map(tuple, state))][action] = new_q

    def decay_exploration(self):
        self.exploration_rate *= self.decay_rate
