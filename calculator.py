def add(a,b):
    c = a + b
    return print(f"Your answer is {c}")

def subtract(a,b):
    c = a - b
    return print(f"Your answer is {c}")

def divide(a,b):
    c = a / b
    return print(f"Your answer is {c}")

def multiply(a,b):
    c = a * b
    return print(f"Your answer is {c}")

def check_for_exit(input):
    if input == 'e':
        print("Closing calculator!")
        exit()

def validate_user_int_input(int_input):
    if int_input != int():
        return True

def validate_user_operation_input(operation_input):
    valid_input = ['a','s','m','d','e']
    return operation_input not in valid_input

while True:
    
    try:
        user_input_1 = int(input("Please provide a number: "))
    except ValueError:
        print("Invalid Input! Please provide an integer.")
        break

    try:    
        user_input_2 = int(input("Please provide another number: "))
    except ValueError:
        print("Invalid Input! Please provide an integer.")
        break
        
    print("Enter 'e' to exit.")
    user_input_operation = input(
        "What operation do you want to perform? \
Enter 'a' for addition, 's' for subtraction, 'd' for division, 'm' for multiplication: "
    ).lower()
    
    check_for_exit(user_input_operation)

    if validate_user_operation_input(user_input_operation) == True:
        print("Please provide valid input.")
        break

    if user_input_operation == 'a':
        add(user_input_1, user_input_2)

    elif user_input_operation == 's':
        subtract(user_input_1, user_input_2)

    elif user_input_operation == 'd':
        divide(user_input_1, user_input_2)

    elif user_input_operation == 'm':
        multiply(user_input_1, user_input_2)

    

