# tictactoe_ui.py
import tkinter as tk
from tkinter import messagebox
from agent import QLearningAgent
from environment import TicTacToe


class TicTacToeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI")
        self.root.geometry("400x450")
        self.root.configure(bg="#333")  # Background color for the window

        # Initialize board buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

        # Initialize AI and environment
        self.env = TicTacToe()
        self.agent = QLearningAgent()
        self.reset_game()

    def create_board(self):
        """Creates the button grid for the Tic-Tac-Toe board."""
        frame = tk.Frame(self.root, bg="#333")
        frame.pack(pady=20)

        for i in range(3):
            for j in range(3):
                button = tk.Button(frame, text='', font=('Arial', 24), width=5, height=2,
                                   bg="#f0f0f0", fg="#333",
                                   activebackground="#ddd", activeforeground="#111",
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

        # Add reset button with style improvements
        reset_button = tk.Button(self.root, text="Reset Game", font=('Arial', 14),
                                 bg="#4CAF50", fg="white", activebackground="#45A049",
                                 command=self.reset_game)
        reset_button.pack(pady=10)

    def reset_game(self):
        """Resets the game board."""
        self.env.reset()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state=tk.NORMAL, bg="#f0f0f0")

    def on_button_click(self, i, j):
        """Handles button click for player move."""
        if self.env.board[i, j] != 0:
            return

        # Player move
        self.buttons[i][j].config(text='X', bg="#FFC107", disabledforeground="#333")
        self.env.step((i, j), player=1)
        if self.check_game_status():
            return

        # AI move
        ai_action = self.agent.choose_action(self.env.board, self.env.available_actions())
        self.env.step(ai_action, player=-1)
        self.buttons[ai_action[0]][ai_action[1]].config(text='O', bg="#FF5722", disabledforeground="#333")
        self.check_game_status()

    def check_game_status(self):
        """Checks if there's a winner or if it's a draw."""
        if self.env.winner == 1:
            messagebox.showinfo("Game Over", "You Win!")
            self.disable_buttons()
            return True
        elif self.env.winner == -1:
            messagebox.showinfo("Game Over", "AI Wins!")
            self.disable_buttons()
            return True
        elif not self.env.available_actions():
            messagebox.showinfo("Game Over", "It's a Draw!")
            return True
        return False

    def disable_buttons(self):
        """Disables all buttons after the game ends."""
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeUI(root)
    root.mainloop()
