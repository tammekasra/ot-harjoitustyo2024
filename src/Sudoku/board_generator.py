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
        
        This should just check if there are any same numbers that are in COLUMN
        
        '''
        
        for i in range(9):
            if board[i][column] == random_number:
                return False
            
            

        '''
        
        This is the 3x3 grid check - it checks whether there are same numbers in 3x3 grid
        
        '''
        start_row = (row // 3) * 3 # This just takes the row number - 3 // 3 = 0 - we check row 1 and 4 // 3 = 1, we check row 2 and  7//3 = 2 - we check row 3 
        start_column = (column // 3) * 3 # This just takes the column number - 3 // 3 = 0 - we check column 1 and 4 // 3 = 1, we check column 2 and  7//3 = 2 - we check column 3
        for i in range(start_row, start_row + 3): #checks the 3x3 grid
            for j in range(start_column, start_column + 3):
                if board[i][j] == random_number:
                    return False
        
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
    
    
                
        
    