# Tic-Tac-Toe

## Introduction
This repository contains a Tic-Tac-Toe game implementation. The project is divided into three sections:
1. **Playing Tic-Tac-Toe**: Instructions on how to play the game.
2. **Algorithm**: Algorithm to write the game logic.
3. **Structured Code**: Explanation of the code structure.

## Playing Tic-Tac-Toe
Tic-Tac-Toe is a two-player game where each player takes turns marking spaces in a 3x3 grid. The players are represented by the symbols 'X' and 'O'. The goal is to place three of their marks in a horizontal, vertical, or diagonal row. The game ends when one player achieves this goal, or the board is filled without a winner.

### Gameplay:
1. Two players take turns to place their symbols ('X' or 'O') on the board.
2. The first player to align three of their symbols in a row, column, or diagonal wins the game.
3. If all spaces on the board are filled and there is no winner, the game ends in a draw.

## Algorithm
The algorithm for the Tic-Tac-Toe game logic is as follows:
1. Initialize the game board.
2. Write functions to:
   - Check if the board is filled.
   - Check if a player has won.
   - Print the current state of the board.
   - Start the game loop:
     - Randomly select the first player.
     - Iterate until the game ends:
       - Prompt the current player to make a move.
       - Update the board.
       - Check if the current player has won.
       - Check if the board is filled (draw).
       - Switch to the next player.

## Structured Code
The code is structured following the algorithm described above. It includes:
- Initialization of the game board.
- Functions to check for a win, board filled status, and to print the board.
- Implementation of the game loop to handle player moves and game termination.

Feel free to clone this repository and explore the code to understand the implementation details.

## Usage
To play the Tic-Tac-Toe game:
1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the code.
3. Run the Python script `tictactoe.py`.
4. Follow the on-screen instructions to play the game.

## License
This project is licensed under the [MIT License](LICENSE).

