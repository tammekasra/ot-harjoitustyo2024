import pygame #we can later add pygame features like U.I for this
import sys 
from Sudoku import board_generator
from Sudoku import board_generator2
import copy #we need it to copy list twice so we can check the original



class SudokuGame:
    
    '''
    
    We might need this to see if it print out the way we wanted - 9x9 grid
    
    '''
    def print_sudoku_board(board): # This just prints the game - DO NOT USE THIS IN TESTS SINCE WONT ALLOT TO DO THE COMPARISON!
       
        for row in board:
            print(" ".join(map(str, row)))
            
            
            
            
    '''
    This is the pygame set-up
    
    '''
    
    
    '''
    
    
    !!! These codes for pygame were taken from https://github.com/dhhruv/Sudoku-Solver/blob/master/SudokuGUI.py and 
    
    https://github.com/techwithtim/Sudoku-GUI-Solver/blob/master/GUI.py
    
    '''
            
    def display_sudoku_board(board):
        
        
        pygame.init()  #This just initliazes the game - just like for any pygame!
        
        
        
        board2 = copy.deepcopy(board)  # We just need to check which slots we can insert later, so the initial numbers that were generated will not be changed!

       
        screen = pygame.display.set_mode((450, 450)) # screen has length 450 x 450
        
        
        pygame.display.set_caption("Sudoku Game") # This is just the description of the game! 

        
        BLACK = (0, 0, 0) #Just color from pygame document
        WHITE = (255, 255, 255)
        

      
        font = pygame.font.Font(None, 40) #This just allows to insert numbers later on as font

       
        user_input_grid = [[False for _ in range(9)] for _ in range(9)]  # This is just for the input - so we can input the number in correct culmn!

        
        
        
        screen.fill(WHITE) #We just have a white screen - otherwise it's black
        
        
        Game = True
        
        while Game:
            for event in pygame.event.get(): # For the event to start
                
                
                if event.type == pygame.QUIT: # Quit pygame when pressed on X
                    Game = False
                    
                    
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                 
                    mouse = pygame.mouse.get_pos()  #This just gets the position of the mouse
             
                    column = mouse[0] // 50  #We get the column where the mouse is
                    row = mouse[1] // 50  #We get the row where the mouse is
                 
                  
                    
                elif event.type == pygame.KEYDOWN:
                    if pygame.K_1 <= event.key <= pygame.K_9: # We can only press from 1 to 9
                        
                        
                        number = int(pygame.key.name(event.key)) # This didn't work when I didn't have int
                        
                        
                     
                        if (not user_input_grid[row][column]): # This allows to add the number to the column
                            
                            
                            # If the there is 0 in the original sudoku - then add a number - otherwise we would change the whole sudoku
                            if board2[row][column] == 0:
                                board[row][column] = number
                          

           
            
            '''
            
            From here I got copy pasted the ideas from the github to ....
            
            '''
           
            for i in range(9): #This is just for the sudoku board
                for j in range(9):
                    if board[i][j] != 0:
                        text = font.render(str(board[i][j]), True, BLACK)
                        screen.blit(text, (j * 50 + 15, i * 50 + 15))

            
            for i in range(10): #This is only for the grid 
                if i % 3 == 0:
                    pygame.draw.line(screen, BLACK, (50 * i, 0), (50 * i, 450), 4)
                    pygame.draw.line(screen, BLACK, (0, 50 * i), (450, 50 * i), 4)
                else:
                    pygame.draw.line(screen, BLACK, (50 * i, 0), (50 * i, 450), 2)
                    pygame.draw.line(screen, BLACK, (0, 50 * i), (450, 50 * i), 2)

            pygame.display.flip()  #We need to display it
 
        pygame.quit() #We need to quit the game
        
        '''
        Here
        
        '''


    '''
     
    We just take the generated board from board_generator - sudoku board
    
    '''
    sudoku_board = board_generator.BoardGenerator.RandomBoard()
    
    
    '''
    
    Continue from here - we need to take away some numbers from the sudoku_board and add additional tests
    
    '''
    sudoku_board2 = board_generator2.BoardGenerator2.RandomBoard(sudoku_board)
    
    ''' 
    This just prints the sudoku board
    
    '''
    
    display_sudoku_board(sudoku_board2)
    


