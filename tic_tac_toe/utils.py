import numpy as np
import re

list_of_winning_cases = ['123','456','789','147',
                         '258','369','159','357']

def take_and_validate_input_slot(list_of_available_slots):
    """Takes in slot number and validates it, loops until the user provides the accepted input"""
    
    while True:
        try:
            human_selected_slot = str(input("Enter Slot Number: "))            
            if human_selected_slot in list_of_available_slots:
                break
            if human_selected_slot == 'e':
                return 'e'
            if human_selected_slot not in list_of_available_slots:
                print("Please input a available slot.")

        except ValueError:
            print("Invalid Input!")

    return human_selected_slot

def is_win(playing_board_array):
    """Checks the winning cases and if any entries is satisfied returns True"""

    # Horizontal Winning conditions
    if playing_board_array[0][0] == playing_board_array[0][1] \
        and playing_board_array[0][1] == playing_board_array[0][2]:
        winner_letter = playing_board_array[0][0].item()
        return True, winner_letter
    
    elif playing_board_array[1][0] == playing_board_array[1][1] \
        and playing_board_array[1][1] == playing_board_array[1][2]:
        winner_letter = playing_board_array[1][0].item()
        return True, winner_letter
    
    elif playing_board_array[2][0] == playing_board_array[2][1] \
        and playing_board_array[2][1] == playing_board_array[2][2]:
        winner_letter = playing_board_array[2][0].item()
        return True, winner_letter
    
    # Vertical Winning conditions
    elif playing_board_array[0][0] == playing_board_array[1][0] \
        and playing_board_array[1][0] == playing_board_array[2][0]:
        winner_letter = playing_board_array[0][0].item()
        return True, winner_letter
    
    elif playing_board_array[0][1] == playing_board_array[1][1] \
        and playing_board_array[1][1] == playing_board_array[2][1]:
        winner_letter = playing_board_array[0][1].item()
        return True, winner_letter
    
    elif playing_board_array[0][2] == playing_board_array[1][2] \
        and playing_board_array[1][2] == playing_board_array[2][2]:
        winner_letter = playing_board_array[0][2].item()
        return True, winner_letter
    
    # Diagonal Winning conditions
    elif playing_board_array[0][0] == playing_board_array[1][1] \
        and playing_board_array[1][1] == playing_board_array[2][2]:
        winner_letter = playing_board_array[0][0].item()
        return True, winner_letter
    
    elif playing_board_array[0][2] == playing_board_array[1][1] \
        and playing_board_array[1][1] == playing_board_array[2][0]:
        winner_letter = playing_board_array[0][2].item()
        return True, winner_letter
    
    else:
        return False, None

if __name__ == '__main__':
    playing_board_array = np.array([['1','2','a'],['4','5','a'],['7','8','a']])
    result, winner_letter = is_win(playing_board_array)
    print(result, winner_letter)

    """    
        human_selected_slot = '2'
        human_player_letter = 'X'
        for rows in playing_board_array:
            for slot in rows:
                if slot == human_selected_slot:
                    row_id, column_id = np.where(playing_board_array == slot)
                    i = row_id.item()
                    j = column_id.item()
                    playing_board_array[i][j] = human_player_letter

        print(playing_board_array)"""