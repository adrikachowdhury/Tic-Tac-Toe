# Tic-Tac-Toe: Winning Move Detection
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
This compact AI project, developed for an **_Artificial Intelligence (AI)_** course, implements a Tic-Tac-Toe winning move detector using Forward Chaining and First-Order Logic (FOL). It defines a knowledge base with predicates (e.g., `Occupied`, `WinningMove`) to identify if player X can win by placing a mark in an empty position. Optionally, a GUI visualizes the board and AI reasoning, showcasing skills in rule-based AI, logical reasoning, and Python programming for interactive applications.

## Features
- **Forward Chaining**: Applies FOL inference rules to detect winning moves for player X.
- **Knowledge Base**: Defines predicates like `Occupied(P1, X)` and `Empty(P3)` for board state.
- **Win Detection**: Identifies winning moves (e.g., X in P3 with X in P1, P2) using logical rules.
- **GUI (implementation available in another .py file)**: Visualizes the Tic-Tac-Toe board and AI decisions using Tkinter or Pygame.

## Tools
- Python
- NumPy
- Tkinter or Pygame (for GUI)

## Setup
1. Download the repository from GitHub.
2. Install dependencies: numpy
3. Open Tic-Tac-Toe.ipynb in a notebook (Google Colab/Jupyter) and run all cells to implement the game in the console.
4. For GUI version: Open Tic-Tac-Toe (GUI).py in a Python environment (e.g., VS Code or PyCharm) and run the script to launch the GUI game.
