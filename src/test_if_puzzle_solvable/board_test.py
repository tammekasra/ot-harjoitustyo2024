
import unittest 
from Sudoku import board_generator


class TestPrintSudokuBoard(unittest.TestCase):

        
        
    ''' 
    
    This just test whether the generated board is not filled with 0s - since we need a board filled with number from 1 to 10
    
    '''
    
    def test_if_there_are_no_zeros_in_grid(self):
        sudoku_board = board_generator.BoardGenerator.RandomBoard() #we dont need to do the tests via main.... stupid me
    #sudoku_board = main.SudokuGame.sudoku_board
        
        for i in range(9):
            for j in range(9):
                self.assertNotEqual(sudoku_board[i][j], 0, "There should be no zeros in the grid")
                
    '''
    This just checks if there are same numbers on the same ROW
    
    '''
    
    def test_if_there_are_same_numbers_on_the_same_row(self):
        sudoku_board = board_generator.BoardGenerator.RandomBoard()
        
        for i in range(9):
            row = sudoku_board[i] #we checks the rows
        
       
            for j in range(9): #we check the columns
                column = row[j]
                for current_number in range(9): #We don't want that the number we are checking is the same as in the rows!
                    if current_number != j:
                        self.assertNotEqual(column, row[current_number]) #checks if the numbers in the row are not the same!

    '''
    This just check if there are same numbers on the same COLUMN
    '''
    def test_if_there_are_same_numbers_on_the_same_column(self):
        sudoku_board = board_generator.BoardGenerator.RandomBoard()
        
        for i in range(9): 
            column = [sudoku_board[j][i] for j in range(9)] 
            for j in range(9): 
                current_number = column[j]
                for k in range(9): 
                    if k != j:
                        self.assertNotEqual(current_number, column[k])

if __name__ == '__main__':
    unittest.main()



'''
    We might need it later!
    def test_print_sudoku_board(self):
        sudoku_board = main.SudokuGame.sudoku_board #SudokuGame.sudoku_board
        
        
       
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



'''