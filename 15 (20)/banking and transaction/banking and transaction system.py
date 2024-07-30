import random
import datetime
import json 
import os


user_card = dict() # Promting a global dictionary to store all data

def check_password(password: str) -> str:
    """
    This function checks if the provided password matches the confirmation.
    """
    confirmation_password = input("Re-enter the password for confirmation: ")
    if confirmation_password == password:
        print("Password confirmed. You can proceed.")
    else:
        print("Passwords do not match. Please try again.")
        return check_password(password)


def expiring_card_date():
    """
    This function calculates the expiration date for a bank card (6 years from the current date).
    """
    current_date = str(datetime.date.today()).split("-")
    expire_year = str(int(current_date[0]) + 6)
    expire_date = f"{current_date[1]}/{expire_year[2:]}"
    return expire_date


def making_card_number():
    """
    This function generates a random bank card number.
    """
    card_number = str(random.randint(10**15, 9999999999999999))  # generating 16-digit card number 
    formatted_card_number = ' '.join(card_number[i:i+4] for i in range(0, len(card_number), 4))  # formatting card number to make a space after each 4 number
    return formatted_card_number

# Initializing user_card with existing data from "cards.json" if available
if os.path.exists("cards.json"):
    with open("cards.json", "r") as json_file:
        user_card = json.load(json_file)
else: 
    user_card = {}


def opening_bank_card():
    """
    This function opens a new bank card for the user.
    """
    full_name = input("Please enter your full name: ")
    passport_number = input("Please enter your passport number: ")
    password = input("Create any password: ")
    check_password(password=password)

    user_info = {
        "Full name": full_name,
        "Passport number": passport_number,
        "Password": password,
        "Expire date": expiring_card_date()
    }

    your_card = making_card_number()
    user_card[your_card] = user_info

    print(f"You have sucessfully opened a new bank card.\nYour bank account is: {your_card}")
  
    # Writing the entire user_card dictionary to cards.json
    with open("cards.json", "w") as json_file:
        json.dump(user_card, json_file, indent=4)

    return display_menu()


def transfering_money():
    """
    This function transfers money from one bank card to another.
    """
    users_card_number = input("Enter your bank card number: ").strip()
    users_password = input("Enter your password: ")
    money_amount = float(input("Enter the amount to transfer: "))

    # Checking if card number and pasword matches
    if users_card_number in user_card and user_card[users_card_number]["Password"] == users_password:
        user_card[users_card_number]["Balance"] = user_card.get(users_card_number, {}).get("Balance", 0) + money_amount
        print(f"Your transaction has sucessfully been operated. You balance is: {user_card[users_card_number]['Balance']}")
    
        transaction = {
            "Card number": users_card_number,
            "Time": str(datetime.datetime.now()),
            "Amount": money_amount
        }

        # Appending the transaction to transfers.json
        with open("transfers.json", "w") as transfers_file:
            json.dump(transaction, transfers_file, indent=4)
            transfers_file.write("\n")  # Adding a newline for readability
    else:
        print("Invalid card number or password. Transfer failed.")
        while True:
            user_response = int(input("What would you like to do?\n1. Transfer again.\n2. Go to the menu.\n3. Exit.\n>>> "))
            if user_response == 1:
                return transfering_money()
            elif user_response == 2:
                return display_menu()
            elif user_response == 3:
                print("Thank you for using our service. See you!")
                break
            else:
                print("Invalid input. Please choose a valid option.")

    # Writing the updated user_card dictionary to cards.json
    with open("cards.json", "w") as json_file:
        json.dump(user_card, json_file, indent=4)

    return display_menu()


def show_all_card_info():
    """
    This function displays all information about a bank card.
    """
    users_card_number = input("Enter your bank card number: ").strip()
    users_password = input("Enter your password: ")

    # Checking if card number and pasword matches
    if users_card_number in user_card and user_card[users_card_number]["Password"] == users_password:
        card_info = user_card[users_card_number]
        print(f"Full Name: {card_info['Full name']}")
        print(f"Card Number: {users_card_number}")
        print(f"Password: {card_info['Password']}")
        print(f"Balance: {card_info.get('Balance', 0)}")
    else:
        print("Invalid card number or password. Access denied.")
        while True:
            user_response = int(input("What would you like to do?\n1. Get info again.\n2. Go to the menu.\n3. Exit.\n>>> "))
            if user_response == 1:
                return show_all_card_info()
            elif user_response == 2:
                return display_menu()
            elif user_response == 3:
                print("Thank you for using our service. See you!")
                break
            else:
                print("Invalid input. Please choose a valid option.")

    return display_menu()


print("Welcome to a banking and transaction system.")
print("*" * 60)


def display_menu():
    """
    This function displays the main menu and handles user input.
    """

    menu_text = """
    1. Buy a new bank card.
    2. Transfer money to a bank card.
    3. Show all info about card.
    4. Exit.
    """
    print(menu_text)

    user_input = int(input("Please, choose a number from menu: "))

    if user_input == 1:
        opening_bank_card()
    elif user_input == 2:
        transfering_money()
    elif user_input == 3:
        show_all_card_info()
    elif user_input == 4:
        yes_no_input = input("Would you like to quit a program? y or n >>> ")
        if yes_no_input.lower().strip() == "n":
            display_menu()
        else:
            print("Thank you for using our service. See you!")


display_menu()