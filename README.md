# Tic-Tac-Toe
Tic Tac Toe Game
The project work is divided into three different sections. In the first
section, I will get to know how to play the tic-tac-toe game. After
that, I will see an algorithm that helps us to come up with the
game logic. Finally, I will see the structured code and its
explanation.
Playing Tic TAC Toe
There will be two players in a game. Two signs represent each player. The general
signs used in the game are X and O. Finally, there will be a board with 9 boxes.
The gameplay will be as follows.
• First, one user will place their sign in one of the available empty boxes.
• Next, the second user will place their sign in one of the available empty
boxes.
• The goal of the players is to place their respective signs completely rowwise or column-wise, or diagonally.
• The game goes on until a player wins the game or it ended up in a draw
by filling all boxes without a winning match.
Algorithm
I will now discuss the algorithm to write the code. This algorithm will help me to write
code in any programming language of my choice. Let’s see how it’s done.
• Create a board using a 2-dimensional array and initialize each element
as empty.
o You can represent empty using any symbol you like. Here, we are
going to use a hyphen. '-'.
• Write a function to check whether the board is filled or not.
o Iterate over the board and return false if the board contains an
empty sign or else return true.
• Write a function to check whether a player has won or not.
o We have to check all the possibilities that we discussed in the
previous section.
o Check for all the rows, columns, and two diagonals.
• Write a function to show the board as we will show the board multiple
times to the users while they are playing.
• Write a function to start the game.
o Select the first turn of the player randomly.
o Write an infinite loop that breaks when the game is over (either
win or draw).
▪ Show the board to the user to select the spot for the next
move.
▪ Ask the user to enter the row and column number.
▪ Update the spot with the respective player sign.
▪ Check whether the current player won the game or not.
▪ If the current player won the game, then print a winning
message and break the infinite loop.
▪ Next, check whether the board is filled or not.
▪ If the board is filled, then print the draw message and break
the infinite loop.
o Finally, show the user the final view of the board.
I may be able to visualize what’s happening. Don’t worry, even if you didn’t understand
it completely. I will get more clarity once you see the code.
I try the code on interpreter Python according the given instructions should
implemented in my code work.
