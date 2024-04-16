import random
import pygame



class BoardGenerator:
    

    
    ''' 
    This generated a random board using random randint from random
    
    '''
    
    def RandomBoard():
        
        while True:
            
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
            
            for i in range(9): # Need to remember that this is the ROW
                for j in range(9): # Need to remember that this is the COLUMN
                    if sudoku_board[i][j] == 0:
                        for random_number in random.sample(range(1,10),9): #we just go through all the numbers from 1-10 to check if they can be put there
                            if BoardGenerator.valid(sudoku_board, i , j , random_number):
                                sudoku_board[i][j] = random_number
                                
            if BoardGenerator.check_for_zeros(sudoku_board):
                return sudoku_board
            else:
                sudoku_board = [[0 for _ in range(9)] for _ in range(9)]
    
    def valid(board,row,column,random_number):
        
        
        ''' 
        This just checks if the random.randint from Random board has a number on the same ROW - have no idea yet how to do it with columns
        
        '''
        if random_number in board[row]:
            return False
        
        
        '''
        
        This should just check if there are any same numbers that are in column
        
        '''
        
        for i in range(1,9):
            if i == row:
                continue
            if board[i][column] == random_number:
                return False
            
            
        ''' 
        
        I NEED TO IMPLEENT 3X3 GRID CHECK!
        
        '''
        
        return True
    
    
    ''' 
    
    Check for Zeros just checks if there are ny 0s left on the board - if yes, we need to start over
    
    
    '''
    
    
    def check_for_zeros(board):
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return False
                
        return True
                
        
    