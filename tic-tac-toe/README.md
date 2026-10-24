# Tic Tac Toe

A two-player Tic Tac Toe game with a dark-themed graphical interface, built with `customtkinter`.

## Features

- Two players take turns (X starts), and the current turn is shown on top
- Detects a win or a draw and shows the result
- "New game" button to play again without restarting the app

## Code structure

The game logic is separated from the interface:

- `get_winner(board)` and `is_draw(board)` are plain functions that work on a list of 9 cells
- The `TicTacToe` class builds the window and handles clicks

The 8 winning lines are stored once in `WIN_LINES`, instead of being written out as long conditions.

## How to run

```bash
pip install -r requirements.txt
python tic_tac_toe.py
```
