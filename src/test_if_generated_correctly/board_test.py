'''
This board_test.py is just for only testing whether the board is generated correctly according to SUDOKU rules!

'''


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
                        
    ''' 
    
    This just test whether there are any duplicates in 3x3 grid or boxes
    
    '''

    def test_if_there_are_same_numbers_on_the_same_3x3_grid(self):
        
        sudoku = board_generator.BoardGenerator.RandomBoard()
        
        duplicates = self.duplicates_in_grid(sudoku)
        
        self.assertFalse(duplicates, "There are same numbers in the same 3x3 grid.")

    def duplicates_in_grid(self, board):
        for row in range(0, 9, 3): # Iterate over each 3x3 grid
            for column in range(0, 9, 3):
                seen = set() #to check if there are any same number in the grid
                for i in range(row, row + 3):
                    for j in range(column, column + 3):
                        if board[i][j] != 0:
                            if board[i][j] in seen:
                                return True
                            seen.add(board[i][j])
        return False
        
        
