import random

class BoardGenerator2:
    

    def RandomBoard(board):
        for i in range(len(board)): 
            for j in range(len(board[i])):
                if random.random() < 0.30:  # 30% chance of changing it back to 0
                    board[i][j] = 0
        
        return board