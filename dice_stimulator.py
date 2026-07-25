# Built-in Modules
import random

dice_drawing = {
        1: (
            "-------",
            "|     |",
            "|  o  |",
            "|     |",
            "-------",
        ),
        2: (
            "-------",
            "|o    |",
            "|     |",
            "|    o|",
            "-------",
        ),
        3: (
            "-------",
            "|o    |",
            "|  o  |",
            "|    o|",
            "-------",
        ),
        4: (
            "-------",
            "|o   o|",
            "|     |",
            "|o   o|",
            "-------",
        ),
        5: (
            "-------",
            "|o   o|",
            "|  o  |",
            "|o   o|",
            "-------",
        ),
        6: (
            "-------",
            "|o   o|",
            "|o   o|",
            "|o   o|",
            "-------",
        ),

    }

def extract_dice_from_dict():
    """Extract dice from the dictionary"""

    list_of_keys = []
    for key in dice_drawing.keys():
        list_of_keys.append(key)

    return list_of_keys

def roll_dice():
    """Choose a dice from the list of dices"""

    list_of_keys = extract_dice_from_dict()

    dice1 = random.choice(list_of_keys)
    dice2 = random.choice(list_of_keys)

    for i in dice_drawing[dice1]:
        print(i)
        
    for i in dice_drawing[dice2]:
        print(i)

def main():
    """Main function"""
    
    print("Welcome To Dice Stimulator!\n")

    while True:

        user_input = input("Want to roll the dice? Type Yes or No: ").lower()

        if user_input == 'yes':
            roll_dice()

        elif user_input == 'no':
            print("Thank you for using the Dice Stimulator!")
            exit()

        else:
            print("Please provide a valid input.")
            exit()

if __name__ == '__main__':
    main()