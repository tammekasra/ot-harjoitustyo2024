from Sudoku.game import SudokuGame
from Sudoku.ui import UserInterface



if __name__ == "__main__":
    start_board = SudokuGame.sudoku_board2
    UserInterface.display_sudoku_board(start_board)
    


