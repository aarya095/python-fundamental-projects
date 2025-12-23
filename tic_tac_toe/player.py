import random

def assign_x_or_o_to_player():
    """Assigns X or O randomly to either player"""

    human_player = None
    computer_player = None
    x_or_o_choice = ['X','O']

    human_player = random.choice(x_or_o_choice)
    if human_player == 'X':
        computer_player = 'O'
    else:
        computer_player = 'X'

    players_dict = {
        'Human player' : human_player,
        'Computer player' : computer_player
    }

    return players_dict

if __name__ == '__main__':
    player_dict = assign_x_or_o_to_player()
    print(player_dict)