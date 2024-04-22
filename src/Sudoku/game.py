import pygame #we can later add pygame features like U.I for this
import sys 
from Sudoku import board_generator


class SudokuGame:
    def print_sudoku_board(board): # This just prints the game - DO NOT USE THIS IN TESTS SINCE WONT ALLOT TO DO THE COMPARISON!
       
        for row in board:
            print(" ".join(map(str, row)))
    
    
  
        ''' 
        This is an example board we tested if everything was alright
        
        '''
    #sudoku_board = [
    #        [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #        [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #        [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #        [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #        [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #        [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #        [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #        [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #        [0, 0, 0, 0, 8, 0, 0, 7, 9]
     #   ]

        # Prints it
    '''
     
    We just take the generated board from board_generator - sudoku board
    
    '''
    sudoku_board = board_generator.BoardGenerator.RandomBoard()
    
    
    '''
    
    Continue from here - we need to take away some numbers from the sudoku_board and add additional tests
    
    '''
    
    
    ''' 
    This just prints the sudoku board
    
    '''
    print_sudoku_board(sudoku_board)


