
import pygame #we can later add pygame features like U.I for this
import random
from Sudoku import ui2



class UserInterface:
    
    
              
    
    score = 0
    
    BLACK = (0, 0, 0) #Just color from pygame document
    WHITE = (255, 255, 255)
    
    
    
    
    
    
    '''!!! These codes for pygame were taken from https://github.com/dhhruv/Sudoku-Solver/blob/master/SudokuGUI.py and 
    
    https://github.com/techwithtim/Sudoku-GUI-Solver/blob/master/GUI.py
    
    We got the modified codes from here to the end!
    '''
            
    def display_sudoku_board(board,solved_board):
        
        '''
        This just initliazes the game - just like for any pygame!
        '''
        
        
        pygame.init()  
        
        '''
        Screen length 450x450
        '''
       
        screen = pygame.display.set_mode((450, 450)) 
        
        
          
       

        
        
        '''
        The position of the font - we will add text there later on
        '''
      
        font = pygame.font.Font(None, 40) 

       
        user_input_grid = [[False for _ in range(9)] for _ in range(9)]  # This is just for the input - so we can input the number in correct culmn!

        Game = True
        
        while Game:
            for event in pygame.event.get(): # For the event to start
                
                if board == solved_board:
                    Game == False 
                    pygame.quit()
                
                elif event.type == pygame.QUIT: # Quit pygame when pressed on X
                    Game = False
                    
                    
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                 
                    mouse = pygame.mouse.get_pos()  #This just gets the position of the mouse
             
                    column = mouse[0] // 50  #We get the column where the mouse is
                    row = mouse[1] // 50  #We get the row where the mouse is
                    
                              
                elif event.type == pygame.KEYDOWN:
                            
                    if pygame.K_1 <= event.key <= pygame.K_9 or pygame.K_SPACE == event.key or pygame.K_BACKSPACE == event.key: # We can only press from 1 to 9
                        
                        
                        if pygame.K_1 <= event.key <= pygame.K_9 :
                        
                        
                        
                            number = int(pygame.key.name(event.key)) # This didn't work when I didn't have int
                            
                            
                        
                            if (not user_input_grid[row][column]): # This allows to add the number to the column
                                    board[row][column] = number                                 # If the there is 0 in the original sudoku - then add a number - otherwise we would change the whole sudoku
                                    UserInterface.score +=1 
                        
                        else:
                                zeros = []   # This allows to add the number to the column                                
                                for i in range(9):
                                    for j in range(9):
                                        if board[i][j] == 0:
                                            zeros.append((i,j))
                                row_1, col_2 = random.choice(zeros)
                                
                                board[row_1][col_2] = solved_board[row_1][col_2]
                                
                                UserInterface.score -=1 
                                zeros.clear()
    
            screen.fill(UserInterface.WHITE) #We just have a white screen - otherwise it's black
            
            
            pygame.display.set_caption(f"Sudoku Game Score: {UserInterface.score}") # This is just the description of the game! 
            
            


            
            '''
            
            From here I modified the code ....
            
            '''
           
            for i in range(9): #This is just for the sudoku board
                for j in range(9):
                    if board[i][j] != 0:
                        text = font.render(str(board[i][j]), True, UserInterface.BLACK)
                        screen.blit(text, (j * 50 + 15, i * 50 + 15))
                 
                     

            
            for i in range(10): #This is only for the grid 
                if i % 3 == 0:
                    pygame.draw.line(screen, UserInterface.BLACK, (50 * i, 0), (50 * i, 450), 4)
                    pygame.draw.line(screen, UserInterface.BLACK, (0, 50 * i), (450, 50 * i), 4)
                else:
                    pygame.draw.line(screen, UserInterface.BLACK, (50 * i, 0), (50 * i, 450), 2)
                    pygame.draw.line(screen, UserInterface.BLACK, (0, 50 * i), (450, 50 * i), 2)

            pygame.display.flip()  #We need to display it
 
        pygame.quit() #We need to quit the game
        
    
  
                
        
        
    