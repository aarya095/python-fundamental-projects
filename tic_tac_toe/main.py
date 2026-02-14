from game import GameLogic

game_logic = GameLogic()

def run():
    player_1, player_2 = game_logic.select_x_and_o()
    print("Player 1 choice is ",player_1)
    print("Player 2 choice is ",player_2)
    
    two_by_two_board = game_logic.generate_play_board()
    print(two_by_two_board)
    game_logic.check_for_available_sqaures(two_by_two_board)


run()