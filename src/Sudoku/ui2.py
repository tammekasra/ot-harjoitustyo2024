import pygame

class UserInterface2:
    def __init__(self):
        pygame.init()

        self.x_axis = 800
        self.y_axis =  600

        self.screen = pygame.display.set_mode((self.x_axis, self.y_axis))

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        pygame.display.set_caption("Welcome to Sudoku!")

        self.font = pygame.font.Font(None, 32)

        self.username_scores = {}  # Dictionary to store usernames and scores

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
    
    def usernames_and_scores(self):
        self.screen.fill(self.WHITE)
        y_offset = 50
        for username, score in self.username_scores.items():
            user_text = self.font.render(f"{username}: {score}", True, self.BLACK)
            self.screen.blit(user_text, (200, y_offset))
            y_offset += 30
        pygame.display.flip()

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
                        self.input_box()  # Go back to input_box
                    


            

    
    

       

  


