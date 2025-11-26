from modules import functions
from modules import validate_user_input

def main():

    while True:
        print("\n--------------------------")
        print("\nWelcome To Password Manager!\n")

        print("1. Create Entry \n2. View Entry \n3. Update Entry \n4. Remove Entry \n")
        print("Enter '0' to exit.")
        user_choice = validate_user_input.take_and_validate_input_operations()

        if user_choice == 0:
            print("\nThank you for using the Password Manager!")
            break
        if user_choice == 1:
            functions.create_entry()
        elif user_choice == 2:
            functions.view_entry()
        elif user_choice == 3:
            functions.update_entry()           
        elif user_choice == 4:
            functions.remove_entry()

if __name__ == '__main__':
    main()