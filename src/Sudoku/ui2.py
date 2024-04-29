import pygame


class UserInterface2:
   
    pygame.init()

 
    x_axis = 800
    y_axis =  600
    
    
    
    screen = pygame.display.set_mode((x_axis, y_axis))
 

 
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    
    pygame.display.set_caption("Welcome to Sudoku!")

    font = pygame.font.Font(None, 32)


    def input_box(name,difficulty):
        text = ""
        input_name = pygame.Rect(200, 200, 400, 32)
        input_difficulty = pygame.Rect(200, 300, 400, 32) 
        input = True
        while input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input = False
                
                    
                    elif event.key == pygame.K_BACKSPACE:
                        if len(text) == 17:
                            continue
                        else:
                          text = text + " "
                    elif event.key == pygame.K_LEFT:
                        text = text[:-1] #just to get back
                    else:
                        if len(text) == 17:
                            continue
                        else:
                            text = text + event.unicode  #even unicode is the userinput
            UserInterface2.screen.fill(UserInterface2.WHITE)
            pygame.draw.rect(UserInterface2.screen, UserInterface2.BLACK, input_name, 2)
            text_itself = UserInterface2.font.render(name + text, True, UserInterface2.BLACK)
            UserInterface2.screen.blit(text_itself, (input_name.x + 5, input_name.y + 5))
            
            pygame.draw.rect(UserInterface2.screen, UserInterface2.BLACK, input_difficulty,2)
            text_itself2 = UserInterface2.font.render(difficulty, True, UserInterface2.BLACK)
            UserInterface2.screen.blit(text_itself2, (input_difficulty.x + 5, input_difficulty.y + 5))
            
            pygame.display.flip()
            
            
def main():
    game = UserInterface2.input_box("Enter your name: ","Select Difficulty - 1,2 or 3: ")
    pygame.quit()
    

       

  


