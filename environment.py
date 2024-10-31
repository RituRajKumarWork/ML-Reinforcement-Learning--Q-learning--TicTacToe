# environment.py
import numpy as np

class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        """Resets the board to its initial empty state."""
        self.board = np.zeros((3, 3), dtype=int)
        self.done = False
        self.winner = None
        return self.board

    def available_actions(self):
        """Returns a list of available (empty) spaces on the board."""
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def step(self, action, player):
        """Applies the player's move to the board and checks for win or draw."""
        if self.board[action] != 0 or self.done:
            return self.board, -10, True  # Invalid move penalty

        self.board[action] = player
        if self.check_winner(player):
            self.done = True
            self.winner = player
            return self.board, 1, True  # Reward for winning

        if not self.available_actions():
            self.done = True
            return self.board, 0, True  # Draw

        return self.board, 0, False  # No reward, game continues

    def check_winner(self, player):
        """Checks if the player has won."""
        return any(
            np.all(line == player)
            for line in np.vstack([self.board, self.board.T, [self.board.diagonal(), np.fliplr(self.board).diagonal()]])
        )
