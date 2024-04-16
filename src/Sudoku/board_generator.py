import random
import pygame



class BoardGenerator:
    
    ''' 
    We need an empty board where to start generating our own sudoku puzzle
    
    '''
    sudoku_board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    ''' 
    This generated a random board using random randint from random
    
    '''
    
    def RandomBoard():
        
        for i in range(9):
            for j in range(9):
                if BoardGenerator.sudoku_board[i][j] == 0:
                    for random_number in random.sample(range(1,10),9): #we just go through all the numbers from 1-10 to check if they can be put there
                        if BoardGenerator.valid(BoardGenerator.sudoku_board, i , random_number):
                            BoardGenerator.sudoku_board[i][j] = random_number
                            
                    
             #   BoardGenerator.sudoku_board[i][j] = random.randint(1, 9)
                
        return BoardGenerator.sudoku_board
    
    def valid(board,row,random_number):
        
        
        ''' 
        This just checks if the random.randint from Random board has a number on the same ROW - have no idea yet how to do it with columns
        
        '''
        if random_number in board[row]:
            return False
        
        return True
                
        
    