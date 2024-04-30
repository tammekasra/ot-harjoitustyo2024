import copy
from Sudoku.ui import UserInterface
from Sudoku import ui2
from Sudoku import board_generator





if __name__ == "__main__":
    
    
    a = ui2.UserInterface2()
    a.input_box()
    a.run()
   
    #ui2.UserInterface2.input_box()   # This is for the selecting name and difficulty
    
   
    
    solved_board = board_generator.BoardGenerator.RandomBoard()  #This generated a board filled with number - basically the solution
    
    copy_solved_board = copy.deepcopy(solved_board)  #We need this board to get the solutions afterwards - otherwise the the numbers will be modifid later on
    
    start_board = board_generator.BoardGenerator.RandomBoard_delete_random_cells(solved_board) #This removes random numbers out of the grid to solve later!
    
    UserInterface.display_sudoku_board(start_board,copy_solved_board)
    


