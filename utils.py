# utils.py
import numpy as np

def print_board(board):
    """Displays the board with symbols for each cell."""
    for row in board:
        print(" | ".join(['X' if cell == 1 else 'O' if cell == -1 else ' ' for cell in row]))
        print("-" * 9)

def evaluate_performance(agent):
    """Evaluates the agent's performance across multiple games."""
    wins, losses, draws = 0, 0, 0
    # Evaluate the agent and track performance
    return wins, losses, draws
