import random

print("Welcome to Rock-Paper-Scissor!")
print("Enter 'e' to exit.\n")

def is_win():
    while 1 == 1:
        user_input = input("Select one, 'r' for rock, 'p' for paper, 's' for scissor: ").lower()

        if user_input == 'e':
             exit()

        computer_choice = random.choice(['r','p','s'])  
        print(f"Computer's choice is {computer_choice}.")

        if user_input == computer_choice:
            print("Its a tie! Play Again?\n")

        elif (user_input == 'r' and computer_choice == 's') or (user_input == 'p' and computer_choice == 'r') \
            or (user_input == 's' and computer_choice == 'p'):
                print("Congrats! You've won.\n")

        else:
            print("You Lost! Try again?\n")

is_win()
