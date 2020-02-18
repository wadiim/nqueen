from nqueen import is_attacked, solve_n_queen
import unittest

class IsAttackedTest(unittest.TestCase):

    def test_empty_board(self):
        board = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        self.assertFalse(is_attacked(x = 0, y = 0, board = board))

    def test_pos_attacked_horizontally(self):
        board = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [1, 0, 0, 0],
                 [0, 0, 0, 0]]
        self.assertTrue(is_attacked(x = 2, y = 2, board = board))

    def test_pos_attacked_vertically(self):
        board = [[0, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        self.assertTrue(is_attacked(x = 3, y = 1, board = board))

    def test_pos_attacked_on_the_first_diagonal(self):
        board = [[0, 0, 0, 1],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        self.assertTrue(is_attacked(x = 3, y = 0, board = board))

    def test_pos_attacked_on_the_second_diagonal(self):
        board = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 0, 0]]
        self.assertTrue(is_attacked(x = 0, y = 1, board = board))

class SolveNQueenTest(unittest.TestCase):

    def test_single_queen(self):
        self.assertTrue(solve_n_queen(board = [[0]]))

    def test_multiple_queens(self):
        board = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        solution1 = [[0, 0, 1, 0],
                     [1, 0, 0, 0],
                     [0, 0, 0, 1],
                     [0, 1, 0, 0]]
        solution2 = [[0, 1, 0, 0],
                     [0, 0, 0, 1],
                     [1, 0, 0, 0],
                     [0, 0, 1, 0]]
        solve_n_queen(board = board)
        self.assertTrue(board == solution1 or board == solution2)

if __name__ == '__main__':
	unittest.main()