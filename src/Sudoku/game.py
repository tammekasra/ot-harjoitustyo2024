import pygame #we can later add pygame features like U.I for this
import sys 
from Sudoku import board_generator
from Sudoku import board_generator2


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
            
    def display_sudoku_board(board):
        
        
        pygame.init() #We need to initate the pygame 

       
        screen = pygame.display.set_mode((700, 700)) #this is just how big the screen is !
        pygame.display.set_caption("Sudoku Game") #this is just the name of the game - description on top

      
        BLACK = (0, 0, 0) #standard black color
        WHITE = (255, 255, 255) #standard white color
        BLUE = (0, 0, 255) #standard blue color

        # Font
        font = pygame.font.Font(None, 40)

        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the screen
            screen.fill(WHITE)

            # Draw the Sudoku board
            for i in range(9):
                for j in range(9):
                    if board[i][j] != 0:
                        text = font.render(str(board[i][j]), True, BLACK)
                        screen.blit(text, (j * 50 + 15, i * 50 + 15))

            # Draw grid lines
            for i in range(10):
                if i % 3 == 0:
                    pygame.draw.line(screen, BLACK, (50 * i, 0), (50 * i, 450), 4)
                    pygame.draw.line(screen, BLACK, (0, 50 * i), (450, 50 * i), 4)
                else:
                    pygame.draw.line(screen, BLACK, (50 * i, 0), (50 * i, 450), 2)
                    pygame.draw.line(screen, BLACK, (0, 50 * i), (450, 50 * i), 2)

            pygame.display.flip()

        pygame.quit()
    

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
    


