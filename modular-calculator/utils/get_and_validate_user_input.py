def get_and_validate_user_input():
    """Gets and Validates the input for numbers"""
    
    while True:
        try:
            num_1 = float(input("Enter first number: "))
            num_2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid Input! Please provide an integer.")
    
    return num_1, num_2


def get_and_validate_input_index():
    """Gets and Validates the input index"""

    user_operation_choice_validation = [0,1,2,3,4,5,6,7]
    
    while True:
        try:
            user_choice = int(input("Select the operation by index: "))
            if user_choice in user_operation_choice_validation:
                break
            if user_choice not in user_operation_choice_validation:
                print("Please input either 0, 1, 2, 3, 4, 5, 6, or 7.")

        except ValueError:
            print("Invalid Input! Please provide an integer.")

    return user_choice

