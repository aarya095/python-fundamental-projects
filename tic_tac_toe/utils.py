import numpy as np

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

def is_win(playing_board_array, list_of_available_slots):
    """Checks the winning cases and if any entries is satisfied returns True"""

    if len(list_of_available_slots) == 0:
        print("Its a tie!")
        return 'tie', None

    # Horizontal Winning conditions
    elif playing_board_array[0][0] == playing_board_array[0][1] \
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
    """    playing_board_array = np.array([['1','2','a'],['4','5','a'],['7','8','a']])
    result, winner_letter = is_win(playing_board_array)
    print(result, winner_letter)"""

    list_2d_mat = [[1,2,3],[4,5,6],[7,8,9]]
    index = list_2d_mat[1].index(6)
    print(index)
    #print(list_2d_mat[0][0])

    numpy_2d_mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(numpy_2d_mat)
