# Third Party Modules
from colorama import Fore, Style

# Local Modules
from calculator.add import Add
from calculator.subtract import Subtract
from calculator.multiply import Multiply
from calculator.divide import Divide
from engine.calculator_engine import CalculatorEngine
from utils import get_and_validate_user_input as get_and_validate

def main():
    """Main function"""

    engine = CalculatorEngine()
    print(Fore.LIGHTGREEN_EX)
    print("░█▀▀░█▀█░█░░░█▀▀░█░█░█░░░█▀█░▀█▀░█▀█░█▀▄")
    print("░█░░░█▀█░█░░░█░░░█░█░█░░░█▀█░░█░░█░█░█▀▄")
    print("░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀")

    while True:
        print(Fore.LIGHTCYAN_EX, Style.BRIGHT + "\n------------------------\n")
        print("1. Addition \n2. Subtraction")
        print("3. Multiply \n4. Divide")
        print("Enter 0 to exit.\n")

        operation_input = get_and_validate.get_and_validate_input_index()

        if operation_input == 0:
            break

        num_1, num_2 = get_and_validate.get_and_validate_user_input()

        # Checks User input and performs the task
        
        if operation_input == 1:
            result = engine.execute_operation(Add(num_1, num_2))
            print(f"Result: {result}")

        elif operation_input == 2:
            result = engine.execute_operation(Subtract(num_1, num_2))
            print(f"Result: {result}")

        elif operation_input == 3:
            result = engine.execute_operation(Multiply(num_1, num_2))
            print(f"Result: {result}")

        elif operation_input == 4:
            try:
                result = engine.execute_operation(Divide(num_1, num_2))
            except ZeroDivisionError:
                print("You can't divide a number by zero!")
                print("\n------------------------")
                continue
            print(f"Result: {result}")

    print(Fore.LIGHTGREEN_EX)
    print("╔═╗┌─┐┌─┐┬  ┬┌─┐┌─┐┌┬┐┬┌─┐┌┐┌  ╔═╗┬  ┌─┐┌─┐┌─┐┌┬┐")
    print("╠═╣├─┘├─┘│  ││  ├─┤ │ ││ ││││  ║  │  │ │└─┐├┤  ││")
    print("╩ ╩┴  ┴  ┴─┘┴└─┘┴ ┴ ┴ ┴└─┘┘└┘  ╚═╝┴─┘└─┘└─┘└─┘─┴┘")
    print("\n------------------------")

if __name__ == '__main__':
    main()
