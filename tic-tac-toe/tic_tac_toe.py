"""Two-player Tic Tac Toe with a customtkinter GUI.

The game logic (get_winner, is_draw) is kept separate from the GUI, so it can
be reused later, for example by a computer opponent.
"""

import customtkinter as ctk

# The 8 winning lines, as indexes into the board (0-8, left to right, top to bottom)
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


# --- Game logic -------------------------------------------------------------

def get_winner(board):
    """Return "X" or "O" if that player has three in a row, otherwise None."""
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    """Return True if the board is full and nobody has won."""
    return all(board) and get_winner(board) is None


# --- GUI --------------------------------------------------------------------

class TicTacToe:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.app = ctk.CTk()
        self.app.geometry("600x540")
        self.app.title("Tic Tac Toe")

        self.board = [""] * 9
        self.current_player = "X"
        self.message = None

        self.turn_label = ctk.CTkLabel(master=self.app, text="", font=("Arial", 24))
        self.turn_label.pack(pady=(15, 5))

        self.frame = ctk.CTkFrame(master=self.app, width=490, height=375, corner_radius=15)
        self.frame.pack(pady=5)

        self.buttons = []
        for i in range(9):
            row, col = divmod(i, 3)
            button = ctk.CTkButton(
                master=self.frame, width=110, height=85, corner_radius=8,
                fg_color="#a1c0dd", hover_color="#7da8d0", text="",
                command=lambda i=i: self.on_click(i),
            )
            button.place(x=50 + 143 * col, y=30 + 115 * row)
            self.buttons.append(button)

        self.restart_button = ctk.CTkButton(
            master=self.app, width=160, height=40, text="New game", command=self.reset,
        )
        self.restart_button.pack(pady=15)

        self.update_turn_label()

    def on_click(self, index):
        """Place the current player's mark in the chosen cell."""
        self.board[index] = self.current_player
        self.buttons[index].configure(
            text=self.current_player, font=("Arial", 40), state="disabled"
        )

        winner = get_winner(self.board)
        if winner:
            self.end_game(f"{winner} wins :)", "#00f96c")
        elif is_draw(self.board):
            self.end_game("Draw =]", "#fca4bb")
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            self.update_turn_label()

    def end_game(self, text, color):
        """Show the result message and lock the board."""
        self.message = ctk.CTkLabel(
            master=self.frame, width=300, height=135, corner_radius=20,
            bg_color=color, text=text, text_color="black", font=("Arial", 40),
        )
        self.message.place(x=95, y=120)
        for button in self.buttons:
            button.configure(state="disabled")
        self.turn_label.configure(text="Game over")

    def reset(self):
        """Start a new game."""
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.configure(text="", state="normal")
        if self.message is not None:
            self.message.destroy()
            self.message = None
        self.update_turn_label()

    def update_turn_label(self):
        self.turn_label.configure(text=f"Turn: {self.current_player}")

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    TicTacToe().run()
