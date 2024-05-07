
from Sudoku import user_interface




if __name__ == "__main__":
    
    
    '''
    game initializes the userinterface for the sudoku game from user_interface.py and generates a sudoku board from 
    
    board_generator.py
    
    '''
    
    
    
    game = user_interface.UserInterface2()
    
    
    game_loop = True
    
    
    '''
    We need to have the game in a loop!
    
    '''
    
    while game_loop:
    
        game.input_box()
        
        game.run()

    
    



