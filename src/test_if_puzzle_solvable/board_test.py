
import unittest 
from Sudoku.game import SudokuGame  # Import the sudoku game itself to do the tests
import main


class TestPrintSudokuBoard(unittest.TestCase):
    def test_print_sudoku_board(self):
        sudoku_board = main.SudokuGame.sudoku_board #SudokuGame.sudoku_board
        
        
        ''' 
        
        We might need it later - we just tested if a random board indeed works as a test
        '''
       # expected_board = [
       #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
       #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
       #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
       #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
       #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
       #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
       #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
       #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
       #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
       # ]
        
        expected_board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertEqual(sudoku_board, expected_board)


if __name__ == '__main__':
    unittest.main()
