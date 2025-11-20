import random
import string


user_choice = []
lowercause_alphabets = string.ascii_lowercase
uppercase_alphabets = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

def validate_length_of_characters(number_of_characters):
    if number_of_characters < 8 or number_of_characters > 32:
        print("Please provide a number between 8 and 32.")
        exit()
    else:
        pass

def take_user_choice():

    number_of_characters = 8
    include_numbers = -1
    include_lower_case = -1
    include_upper_case = -1
    include_symbols = -1

    print("Please input password length atleast 8 characters and atmost 32 characters.")
    try:    
        number_of_characters = int(input("Length of Password: "))
        validate_length_of_characters(number_of_characters)
    except ValueError:
        print("Invalid input. Please provide a number between 8 and 32.")
        exit()

    print("Enter '1' to say yes, and '0' to say no.")

    try:
        include_numbers = int(input("Do you want to include numbers: "))
        include_lower_case = int(input("Do you want to include lower case characters: "))
        include_upper_case = int(input("Do you want to include upper case characters: "))
        include_symbols = int(input("Do you want to include symbols: "))
    except ValueError:
        print("Invalid Input. Please input either 1 or 0.")
        exit()

    if include_numbers == 0 and include_lower_case == 0 \
        and include_upper_case == 0 and include_symbols == 0:
        print("You need to at least select one option.")
        print("Please re-run the program.")
        exit()

    if include_numbers == 1:
        user_choice.append(string.digits)

    if include_lower_case == 1:
        user_choice.append(string.ascii_lowercase)
        
    if include_upper_case == 1:
        user_choice.append(string.ascii_uppercase)
        
    if include_symbols == 1:
        user_choice.append(string.punctuation)
    
    user_choice_str = ''.join(user_choice)
    
    return user_choice_str, number_of_characters

def generate_password(user_choice_str, number_of_characters):

    password = []
    for i in range(number_of_characters):
        password.append(random.choice(user_choice_str))
    password_str = ''.join(password)
    return password_str

def run():
    """Connects all the functions and runs them all together to effectively generate the password."""
    print("Welcome to Password Generator!\n")
    user_choice, number_of_characters = take_user_choice()
    password = generate_password(user_choice, number_of_characters)
    print(f"Password: {password}")

run()


    
    