

import unittest
import pygame
from unittest.mock import MagicMock
from Sudoku.user_interface import UserInterface2


'''

This test_UserInterface is used for testing whether the U.I actually works using MagicMock!

'''
class TestUserInterface(unittest.TestCase):
    
    ''' 
    We just initialize the UserInterface
    
    '''
    def setUp(self):
        self.ui = UserInterface2()
        
        
    '''
    
    This allows to check whether whenever we start a game - then we can check if the scoreboard is indeed empty = "{}"
    
    '''    

    def test_scores_initialization(self):
        self.assertEqual(self.ui.username_scores, {})
        
        
    '''
    
    In order to get the process to be handled - we need to iniate MagicMock, then press keydown, press enter and then we get 
    
    the scores for the empty name "" and the score should be 0!
    
    '''     

    def test_input_process(self):
    
        pygame_event = MagicMock()
        
        pygame_event.type = pygame.KEYDOWN
        
        pygame_event.key = pygame.K_RETURN
        

        with unittest.mock.patch('pygame.event.get', return_value=[pygame_event]):
            scores = self.ui.input_box()

       
        self.assertEqual(scores, {"": 0})
    
  

    
    


