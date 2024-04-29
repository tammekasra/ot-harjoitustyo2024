import unittest 
import copy
from Sudoku.board_generator import BoardGenerator

class TestSudokuSolvable(unittest.TestCase):
        
    def test_if_the_solution_has_an_answer(self):
        random_board = BoardGenerator.RandomBoard()
        modified_board = BoardGenerator.RandomBoard_delete_random_cells(random_board)
        self.assertTrue(solve_sudoku(modified_board))

def solve_sudoku(board):
    
    #if we have reached in our recursion we can simply return True
    if not has_empty_cell(board):
        return True
    row, col = find_empty_cell(board)
    for number in range(0, 9):
        if BoardGenerator.valid(board,row,col,number+1):
            board[row][col] = number+1
            if solve_sudoku(board):
                return True
            else:
                board[row][col] = 0
    #if we dont find any solutions we can just return false
    return False

def has_empty_cell(board):
    for row in board:
        if 0 in row:
            return True
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


        