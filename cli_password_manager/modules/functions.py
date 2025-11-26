import json
import time
import modules.validate_user_input as validate_input

def take_usrname_and_password():
    input_username = input("Enter username: ")
    input_password = validate_input.take_and_validate_input_password()
    timestamp = time.strftime("%d-%m-%Y | %H:%M:%S")

    with open('modules/password.py','r') as f:
        password_data = json.load(f)

    return password_data, input_username, input_password, timestamp

def create_entry():
    """Creates an entry to be added to the json file"""
    password_data, input_username, input_password, timestamp = take_usrname_and_password()
    password_data.append({'Username': input_username,'Password':input_password, "Time created":timestamp})
    with open('modules/password.py','w') as f:
        json.dump(password_data, f, indent=3)
    
    print("Entry created successfully!")
    
    return password_data

def view_entry():
    with open('modules/password.py','r') as f:
        password_data = json.load(f)
    i = 1
    for entry in password_data:
        print(f"\n{i}.")
        for key, value in entry.items():
            print(f"{key} : {value}")
        i += 1

def update_entry():
    """Updates the password entry"""
    with open('modules/password.py','r') as f:
        password_data = json.load(f)
    i = 1
    for entry in password_data:
        print(f"{i}. ",entry['Username'])
        i += 1
    user_choice_for_updation = int(input(f"Choose the number of entry you want to modify \n i.e. from 1 to {len(password_data)}: "))
    index = user_choice_for_updation - 1

    for entry in range(len(password_data)):
        if entry == index:
            password_data, input_username, input_password, timestamp = take_usrname_and_password()
            password_data[index] = {'Username': input_username,'Password':input_password, "Time created":timestamp}
            break
    with open('modules/password.py','w') as f:
        json.dump(password_data, f, indent=3)

    print(f"Entry number '{index}' updated successfully!")

def remove_entry():
    """Deletes an entry"""
    with open('modules/password.py','r') as f:
        password_data = json.load(f)
    i = 1
    for entry in password_data:
        print(f"{i}. ",entry['Username'])
        i += 1
    user_choice_for_updation = int(input(f"Choose the number of entry you want to delete \n i.e. from 1 to {len(password_data)}: "))
    index = user_choice_for_updation - 1

    for entry in range(len(password_data)):
        if entry == (index):
            del password_data[index]
    with open('modules/password.py','w') as f:
        json.dump(password_data, f, indent=3)
    print(f"Entry number '{user_choice_for_updation}' deleted successfully!")
