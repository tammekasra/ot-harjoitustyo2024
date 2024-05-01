import pygame
import random
import copy
from Sudoku import board_generator


class UserInterface2:
    
    '''
    
    
    Here we initiate the game, get a random board to solve and all the initial sizes of the screens!
    
    '''
    def __init__(self):
        pygame.init()

        self.x_axis = 800
        self.y_axis =  600
        self.solved_board = board_generator.BoardGenerator.RandomBoard() 
    
        self.copy_solved_board = copy.deepcopy(self.solved_board)
    
        self.start_board = board_generator.BoardGenerator.RandomBoard_delete_random_cells(self.solved_board)

        self.screen = pygame.display.set_mode((self.x_axis, self.y_axis))
        
        self.screen_display = pygame.display.set_mode((800, 600)) 
        

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        pygame.display.set_caption("Welcome to Sudoku!")

        self.font = pygame.font.Font(None, 32)

        self.username_scores = {}  # Dictionary to store usernames and scores
        
        self.score = 0
        
    ''' 
    This is the samll box where the name will be written!
    
    '''

    def input_box(self):
        text = ""
        input_name = pygame.Rect(200, 200, 400, 32)
        input = True
        prompt = "Enter your name: "

        while input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input = False
                        self.username_scores[text] = 0  # Initialize score to 0
                    elif event.key == pygame.K_BACKSPACE:
                        if len(text) == 17:
                            continue
                        else:
                            text = text + " "
                    elif event.key == pygame.K_LEFT:
                        return self.input_box()  # Go back to input_box
                    else:
                        if len(text) == 17:
                            continue
                        else:
                            text = text + event.unicode  # user input
            self.screen.fill(self.WHITE)
            pygame.draw.rect(self.screen, self.BLACK, input_name, 2)
            text_itself = self.font.render(prompt + text, True, self.BLACK)
            self.screen.blit(text_itself, (input_name.x + 5, input_name.y + 5))

            pygame.display.flip()

        return self.username_scores  
    
    
    '''
    
    This just shows the all the usernames with their scores as display and updates it!
    '''
    
    def usernames_and_scores(self):
        self.screen.fill(self.WHITE)
        y_offset = 50
        for username, score in self.username_scores.items():
            user_text = self.font.render(f"{username}: {score}", True, self.BLACK)
            self.screen.blit(user_text, (200, y_offset))
            y_offset += 30
        pygame.display.flip()
        
    '''
    This displays all the usernames and their scores!
    
    '''

    def run(self):
        while True:
            self.usernames_and_scores()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    elif event.key == pygame.K_LEFT:
                        return self.input_box()  # Go back to input_box
                    elif event.key == pygame.K_RIGHT:
                        return self.display_sudoku_board()
    
    '''!!! These codes for pygame were taken from https://github.com/dhhruv/Sudoku-Solver/blob/master/SudokuGUI.py and 
    
    https://github.com/techwithtim/Sudoku-GUI-Solver/blob/master/GUI.py
    
    We got the modified codes from here to the end!
    '''
            
    def display_sudoku_board(self):
        
        '''
        This just initliazes the game - just like for any pygame!
        '''
        
        
        pygame.init()  
        
        '''
        Screen length 450x450
        '''
       
        screen_sudoku = pygame.display.set_mode((450, 450)) 
        
        
          
       

        
        
        '''
        The position of the font - we will add text there later on
        '''
      
        font = pygame.font.Font(None, 40) 

       
        user_input_grid = [[False for _ in range(9)] for _ in range(9)]  # This is just for the input - so we can input the number in correct culmn!

        Game = True
       
        while Game:
            for event in pygame.event.get(): # For the event to start
                
                
                if self.start_board == self.copy_solved_board:
                    Game == False 
                    return self.run()
                
                elif event.type == pygame.QUIT: # Quit pygame when pressed on X
                    Game = False
                    return self.run()
                    
                    
                    
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                 
                    mouse = pygame.mouse.get_pos()  #This just gets the position of the mouse
             
                    column = mouse[0] // 50  #We get the column where the mouse is
                    row = mouse[1] // 50  #We get the row where the mouse is
                    
                              
                elif event.type == pygame.KEYDOWN:
                            
                    if pygame.K_1 <= event.key <= pygame.K_9 or event.key == pygame.K_LEFT or pygame.K_SPACE == event.key or pygame.K_BACKSPACE == event.key: # We can only press from 1 to 9
                        
                        if event.key == pygame.K_LEFT:
                            return self.run()
                        if pygame.K_1 <= event.key <= pygame.K_9 :
                        
                        
                        
                            number = int(pygame.key.name(event.key)) # This didn't work when I didn't have int
                            
                            
                        
                            if (not user_input_grid[row][column]): # This allows to add the number to the column
                                    self.start_board[row][column] = number                                 # If the there is 0 in the original sudoku - then add a number - otherwise we would change the whole sudoku
                                    self.score +=1 
                        
                        else:
                                zeros = []   # This allows to add the number to the column                                
                                for i in range(9):
                                    for j in range(9):
                                        if self.start_board[i][j] == 0:
                                            zeros.append((i,j))
                                row_1, col_2 = random.choice(zeros)
                                
                                self.start_board[row_1][col_2] = self.copy_solved_board[row_1][col_2]
                                
                                self.score -=1 
                                zeros.clear()
    
            screen_sudoku.fill(self.WHITE) #We just have a white screen - otherwise it's black
            
            
            pygame.display.set_caption(f"Sudoku Game Score: {self.score}") # This is just the description of the game! 
            
            


            
            '''
            
            From here I modified the code ....
            
            '''
           
            for i in range(9): #This is just for the sudoku board
                for j in range(9):
                    if self.start_board[i][j] != 0:
                        text = font.render(str(self.start_board[i][j]), True, self.BLACK)
                        screen_sudoku.blit(text, (j * 50 + 15, i * 50 + 15))
                 
                     

            
            for i in range(10): #This is only for the grid 
                if i % 3 == 0:
                    pygame.draw.line(screen_sudoku, self.BLACK, (50 * i, 0), (50 * i, 450), 4)
                    pygame.draw.line(screen_sudoku, self.BLACK, (0, 50 * i), (450, 50 * i), 4)
                else:
                    pygame.draw.line(screen_sudoku, self.BLACK, (50 * i, 0), (50 * i, 450), 2)
                    pygame.draw.line(screen_sudoku, self.BLACK, (0, 50 * i), (450, 50 * i), 2)

            pygame.display.flip()  #We need to display it
 
        pygame.quit() #We need to quit the game
                        



            
