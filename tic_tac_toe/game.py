import random
import numpy as np

class GameLogic:
    def __init__(self):

        self.player_1  = ''
        self.player_2  = ''
        
    def select_x_and_o(self):
        """
        Assigns each player with either X or O
        """

        x_and_o = ['X','O']

        player_1 = ''
        player_2 = ''

        player_1 = random.choice(x_and_o)

        if player_1 == 'X':
            player_2 = 'O'

        else:
            player_2 = 'X'

        return player_1, player_2
    
    def reference_board(self):
        """
        Prints a reference board
        """
        
        reference_two_by_two_board = [['1','2','3'], ['4','5','6'], ['7','8','9']]
        return reference_two_by_two_board
    
    def generate_play_board(self):
        """
        Generates the Play Board
        """

        two_by_two_board = np.array([['','',''],['','',''],['','','']])

        print(f" {two_by_two_board[0,0]} |  {two_by_two_board[0,1]}  | {two_by_two_board[0,2]} ")
        print("---|-----|---")
        print(f" {two_by_two_board[1,0]} |  {two_by_two_board[1,1]}  | {two_by_two_board[1,2]} ")
        print("---|-----|---")
        print(f" {two_by_two_board[2,0]} |  {two_by_two_board[2,1]}  | {two_by_two_board[2,2]} ")

        return two_by_two_board

    def check_for_available_squares(self, two_by_two_board):
        """
        Checks for the available squares where the player can mark
        """

        for row in two_by_two_board:
            print(type(row))
            print(two_by_two_board.index(row))
            for column in row:
                print(type(column))
                print(row.index(column))