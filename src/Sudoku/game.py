import pygame #we can later add pygame features like U.I for this
import sys 
from Sudoku import board_generator


class SudokuGame:
    def print_sudoku_board(board): # This just prints the game - DO NOT USE THIS IN TESTS SINCE WONT ALLOT TO DO THE COMPARISON!
       
        for row in board:
            print(" ".join(map(str, row)))


        # Example Sudoku board just for testing
    sudoku_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        # Prints it
    print_sudoku_board(sudoku_board)


