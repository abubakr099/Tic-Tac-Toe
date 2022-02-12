import unittest
from tictactoe import TicTacToe as ttt

class TestTicTacToe(unittest.TestCase):

	def setUp(self):
		"""Test object that will be used to perform test on its methods and variables"""
		self.game = ttt()
		
	def test_create_board(self):
		"""Tests weather the board has been generated"""
		expected_val = [list(3*"-"), list(3*"-"), list(3*"-")]
		self.game.create_board()
		actual_val = self.game.board
		self.assertEqual(expected_val, actual_val)

	def test_get_random_first_player(self):
		"""Checks if the correct range is selected"""
		self.assertIn(self.game.get_random_first_player(), (0, 1))

	def test_fix_spot(self):
		"""Check the players selected position"""
		self.game.create_board()
		self.game.fix_spot(2, 2, "X")
		self.assertEqual(self.game.board[2][2], "X")

	def test_swap_player_turn(self):
		"""Makes sure its the turn of the other player"""
		self.assertEqual(self.game.swap_player_turn("X"), "O")

	def test_is_board_filled(self):
		"""Check if there are unfilled spots left"""
		self.game.create_board()
		self.assertIn("-", " ".join(" ".join(s) for s in self.game.board))

	def test_is_player_win(self):
		"""Checks if the specified player has won"""
		self.game.create_board()
		self.game.board[0] = ["X", "X", "X"]
		self.assertEqual(self.game.board[0], ["X", "X", "X"])

if __name__ == "__main__":
	unittest.main()

