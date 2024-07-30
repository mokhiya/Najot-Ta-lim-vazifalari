from registeruser import register_user, login_user
from chatfeatures import create_chat, join_chat, delete_chat, show_created_chats, show_joined_chats


def second_menu():
    """Main menu for logged-in users."""
    while True:
        text = """
        1. Create chat | chat_code -> chat random id 
        2. Join the chat | -> chat_password, chat_code 
        3. Delete chat | chat_code 
        4. Show my created chats 
        5. Show my joined chats 
        6. Exit """
        print(text)
        user_input = int(input("Choose a number from the menu: "))

        if user_input == 1:
            create_chat()
        elif user_input == 2:
            join_chat()
        elif user_input == 3:
            delete_chat()
        elif user_input == 4:
            show_created_chats()
        elif user_input == 5:
            show_joined_chats()
        elif user_input == 6:
            print("You have exited the program. See you!")
            break
        else:
            print("Choose a proper number!")


def display_main_menu():
    """Main menu for the application."""
    while True:
        text = """
        1. Register.
        2. Login.
        3. Exit. """
        print(text)
        user_input = int(input("Choose a number from the menu: "))

        if user_input == 1:
            if register_user():
                continue
        elif user_input == 2:
            if login_user():
                second_menu()
        elif user_input == 3:
            print("You have exited the program. See you!")
            break
        else:
            print("Choose a proper number!")

if __name__ == "__main__":
    display_main_menu()
