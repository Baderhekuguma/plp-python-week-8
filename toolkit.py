# ==========================================
# Personal Mini-Toolkit - Week 8 Final Project
# Welcoming message
# ==========================================
print("Welcome to your Personal Mini-Toolkit! Let's get things done.")

# Initialize a list for our shopping list tool (used in Tool 3)
shopping_list = []

# Main menu loop (Runs until the user chooses to quit)
while True:
    print("\n=== PERSONAL MINI-TOOLKIT MENU ===")
    print("1. Number Guessing Game")
    print("2. Simple Calculator")
    print("3. My Shopping List")
    print("4. Quit")
    
    choice = input("Enter your choice (1-4): ")
    
    # Tool 1: Number Guessing Game (Uses a loop and conditionals)
    if choice == "1":
        print("\n--- Tool 1: Number Guessing Game ---")
        secret_number = 7
        guess = int(input("Guess a number between 1 and 10: "))
        
        while guess != secret_number:
            print("Incorrect! Try again.")
            guess = int(input("Guess a number between 1 and 10: "))
            
        print(f"🎉 Correct! You guessed the secret number {secret_number}!")

    # Tool 2: Simple Calculator (Uses conditionals and f-strings)
    elif choice == "2":
        print("\n--- Tool 2: Simple Calculator ---")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ")
        
        if op == "+":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif op == "-":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif op == "*":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif op == "/" and num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operation or division by zero!")

    # Tool 3: My Shopping List (Uses a changing list and a loop)
    elif choice == "3":
        print("\n--- Tool 3: My Shopping List ---")
        while True:
            print("\n1. View List")
            print("2. Add Item")
            print("3. Back to Main Menu")
            sub_choice = input("Choose an option (1-3): ")
            
            if sub_choice == "1":
                if len(shopping_list) == 0:
                    print("Your shopping list is currently empty.")
                else:
                    print("Current Shopping List:")
                    for index, item in enumerate(shopping_list, 1):
                        print(f"{index}. {item}")
            elif sub_choice == "2":
                new_item = input("Enter item to add: ")
                shopping_list.append(new_item)
                print(f"Added '{new_item}' to your list!")
            elif sub_choice == "3":
                break
            else:
                print("Invalid choice, please select 1, 2, or 3.")

    # Quit Option
    elif choice == "4":
        print("\nThank you for using Personal Mini-Toolkit. Goodbye! 👋")
        break

    # Handling Invalid Menu Choices gracefully (so the program doesn't crash)
    else:
        print(f"\n❌ '{choice}' is not a valid option. Please enter a number between 1 and 4.")