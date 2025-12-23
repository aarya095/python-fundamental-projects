import random

from player import assign_x_or_o_to_player
from utils import *

def generate_playing_board(playing_board_array):
    """Generates the playing board using the 2d array"""
    print("-----------")
    print(f"|{playing_board_array[0][0]} | {playing_board_array[0][1]} | {playing_board_array[0][2]}|")
    print("|--|---|--|")
    print(f"|{playing_board_array[1][0]} | {playing_board_array[1][1]} | {playing_board_array[1][2]}|")
    print("|--|---|--|")
    print(f"|{playing_board_array[2][0]} | {playing_board_array[2][1]} | {playing_board_array[2][2]}|")
    print("-----------")

def computer_play(playing_board_array, computer_player_letter, 
                  list_of_available_slots, computer_player_selected_slots):
    """Makes the computer play"""
    computer_selected_slot = random.choice(list_of_available_slots)
    print(computer_selected_slot)
    index_of_slot = list_of_available_slots.index(computer_selected_slot)
    pop_selected_slot = list_of_available_slots.pop(index_of_slot)
    computer_player_selected_slots.append(pop_selected_slot)

    for rows in playing_board_array:
        for slot in rows:
            if slot == computer_selected_slot:
                row_id, column_id = np.where(playing_board_array == slot)
                i = row_id.item()
                j = column_id.item()
                print(i,j)
                playing_board_array[i][j] = computer_player_letter

def human_play(playing_board_array, human_player_letter, 
               list_of_available_slots, human_player_selected_slots):
    """Makes the human play"""
    human_selected_slot = take_and_validate_input_slot(list_of_available_slots)

    if human_selected_slot == 'e':
        exit()

    index_of_slot = list_of_available_slots.index(human_selected_slot)
    pop_selected_slot = list_of_available_slots.pop(index_of_slot)
    human_player_selected_slots.append(pop_selected_slot)

    for rows in playing_board_array:
        for slot in rows:
            if slot == human_selected_slot:
                row_id, column_id = np.where(playing_board_array == slot)
                i = row_id.item()
                j = column_id.item()
                playing_board_array[i][j] = human_player_letter

def main():
    """Main Function"""
    list_of_available_slots = ['1','2','3','4','5','6','7','8','9']
    human_player_selected_slots = []
    computer_player_selected_slots = []
    playing_board_array = np.array([['1','2','3'],['4','5','6'],['7','8','9']])

    print("Welcome to Tic-Tac-Toe!")
    print("------------------------")
    print("X plays first. Enter 'e' to exit.")
    
    human_player_letter, computer_player_letter = assign_x_or_o_to_player()
    print(f"You have '{human_player_letter}'.")

    if human_player_letter == 'X':
        print("Your turn!")
        while len(list_of_available_slots) != 0:
            generate_playing_board(playing_board_array)

            human_play(playing_board_array, human_player_letter, 
                       list_of_available_slots, human_player_selected_slots)
            
            generate_playing_board(playing_board_array)
            
            result = is_win(human_player_selected_slots)
            if result == True:
                print("Congratulations! You Won!")
                break
            
            computer_play(playing_board_array, computer_player_letter, 
                          list_of_available_slots, computer_player_selected_slots)
            
            result = is_win(computer_player_selected_slots)
            if result == True:
                print("You Lost! Try Again?")
                break

    else:
        print("Computer's turn!")
        while len(list_of_available_slots) != 0:
            generate_playing_board(playing_board_array)

            computer_play(playing_board_array, computer_player_letter, 
                          list_of_available_slots, computer_player_selected_slots)
            
            generate_playing_board(playing_board_array)
            
            result = is_win(computer_player_selected_slots)
            if result == True:
                print("You Lost! Try Again?")
                break
            
            human_play(playing_board_array, human_player_letter, 
                       list_of_available_slots, human_player_selected_slots)
            
            result = is_win(human_player_selected_slots)
            if result == True:
                print("Congratulations! You Won!")
                break
    

if __name__ == '__main__':
    main()