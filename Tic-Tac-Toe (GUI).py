import numpy as np
import tkinter as tk
from tkinter import messagebox

# Set up the game board (3x3 grid with P1 to P9)
board = np.array([["P1", "P2", "P3"],
                  ["P4", "P5", "P6"],
                  ["P7", "P8", "P9"]])

# List to keep track of moves (knowledge base)
knowledge_base = []

# Add a move to the knowledge base
def kb(fact):
    if fact not in knowledge_base:
        knowledge_base.append(fact)

# Check if a player won (rows, columns, diagonals)
def WinningMove(mark):
    win_combinations = [
        [board[0, 0], board[0, 1], board[0, 2]],  # Row 1
        [board[1, 0], board[1, 1], board[1, 2]],  # Row 2
        [board[2, 0], board[2, 1], board[2, 2]],  # Row 3
        [board[0, 0], board[1, 0], board[2, 0]],  # Column 1
        [board[0, 1], board[1, 1], board[2, 1]],  # Column 2
        [board[0, 2], board[1, 2], board[2, 2]],  # Column 3
        [board[0, 0], board[1, 1], board[2, 2]],  # Diagonal 1
        [board[0, 2], board[1, 1], board[2, 0]],  # Diagonal 2
    ]
    for combo in win_combinations:
        if all(pos == mark for pos in combo):
            return True
    return False

# Check if the board is full (draw)
def is_board_full():
    return all(pos == 'O' or pos == 'X' for pos in board.flatten())

# GUI class to make the game window
class TicTacToeGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic-Tac-Toe")
        self.window.configure(bg="#FFE6E6")  # Pastel pink background
        self.turn = "Player1"  # Start with Player 1
        self.mark = 'O'  # Player 1 uses O
        self.buttons = {}  # Store buttons

        # Label to show whose turn it is
        self.status = tk.Label(window, text="Player 1: Place O", font=("Arial", 12),
                               bg="#FFE6E6", fg="#b4312c")  # Pink text
        self.status.grid(row=0, column=0, columnspan=3)

        # Make 3x3 buttons
        for i in range(3):
            for j in range(3):
                btn = tk.Button(window, text=board[i, j], font=("Arial", 20),
                                width=5, height=2, bg="#ffe4de",
                                command=lambda r=i, c=j: self.click(r, c))
                btn.grid(row=i+1, column=j)
                self.buttons[(i, j)] = btn
                # Hover effect: change to lavender
                btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#e5908d"))
                btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#ffe4de"))

    def click(self, r, c):
        position = board[r, c]
        # Only allow clicks on empty spots
        if position not in ['O', 'X']:
            board[r, c] = self.mark  # Place O or X
            self.buttons[(r, c)].config(text=self.mark, bg="#d78380", state="disabled")
            kb(f"Occupied({self.mark}, {position})")  # Track move

            # Check if someone won
            if WinningMove(self.mark):
                self.status.config(text=f"{self.turn} Wins!", fg="#b4312c")  # Yellow
                messagebox.showinfo("Game Over", f"{self.turn} wins!")
                self.disable_all()
            # Check if it’s a draw
            elif is_board_full():
                self.status.config(text="Draw!", fg="#b4312c")  # Yellow
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_all()
            else:
                # Switch players
                self.turn = "Player2" if self.turn == "Player1" else "Player1"
                self.mark = 'X' if self.mark == 'O' else 'O'
                self.status.config(text=f"{self.turn}: Place {self.mark}",
                                  fg="#b4312c" if self.mark == 'O' else "#9f449f")

    def disable_all(self):
        for btn in self.buttons.values():
            btn.config(state="disabled")

# Start the game
if __name__ == "__main__":
    window = tk.Tk()
    game = TicTacToeGUI(window)
    window.mainloop()
    print("Final Knowledge Base:", knowledge_base)
