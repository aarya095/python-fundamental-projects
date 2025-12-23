import numpy as np

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

def is_win(player_selected_slots):
    """Checks the winning cases list and if the player's selected slots matches any entries"""
    player_selected_slots.sort()
    player_selected_slots_str = ""
    for slot in player_selected_slots:
        player_selected_slots_str += str(slot)
    if player_selected_slots_str in list_of_winning_cases:
        return True
    else:
        return False
    

if __name__ == '__main__':
    playing_board_array = np.array([['1','2','3'],['4','5','6'],['7','8','9']])
    human_selected_slot = '2'
    human_player_letter = 'X'
    for rows in playing_board_array:
        for slot in rows:
            if slot == human_selected_slot:
                row_id, column_id = np.where(playing_board_array == slot)
                i = row_id.item()
                j = column_id.item()
                playing_board_array[i][j] = human_player_letter

    print(playing_board_array)