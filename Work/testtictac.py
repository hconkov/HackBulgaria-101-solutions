import unittest

from tictactoe import isBoardFull


class TestTicTac(unittest.TestCase):

    def test_isboardfull(self):
        board = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        self.assertEqual(isBoardfull(board), True)


if __name__ == '__name__':
    unittest.main()
