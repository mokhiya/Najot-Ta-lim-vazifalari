import random
from userclass import User, user_manager, load_users, save_users, current_user


def create_chat():
    """Create a new chat."""
    global current_user

    if current_user is None:
        print("No user is currently logged in. Please log in first.")
        return
    
    chat_password = input("Create your secret chat's password: ")
    generated_code = random.randint(1, 10000)
    print(f"Here is your chat code: {generated_code}")

    chat_data = {
        'code': generated_code,
        'password': chat_password,
        'creator': current_user.username,
        'members': [current_user.username]
    }
    user_manager.add_data(data=chat_data)
    current_user.created_chats.append(chat_data)
    print("You have successfully created a chat!")


def join_chat():
    """Join an existing chat."""
    global current_user
    
    while True:
        chat_password = input("Enter the chat's password: ")
        try:
            generated_code = int(input("Enter the generated chat's code: "))
        except ValueError:
            print("Invalid code. Please enter a valid number.")
            continue

        for chat in user_manager.read():
            if chat['code'] == generated_code:
                if User.hash_password(chat_password) == chat['password']:
                    if current_user.username in chat['members']:
                        print("You are already a member of this chat.")
                    else:
                        chat['members'].append(current_user.username)
                        current_user.joined_chats.append(chat)
                        all_users = load_users("users.json")
                        all_users[current_user.username]['joined_chats'].append(chat)
                        save_users("users.json", all_users)
                        print("Congratulations, you have joined the chat!")
                        break
                else:
                    print("Incorrect password for the chat.")
                break
        else:
            print("Chat code or password did not match.")
            user_input = input("""
Password and code did not match, please choose one of the following options:
1. Create a new chat.
2. Re-enter the password and the code.
""")
            if user_input == "1":
                create_chat()
            else:
                continue


def delete_chat():
    """Delete an existing chat."""
    global current_user
    
    chat_code = int(input("Enter the code of the chat you want to delete: "))
    for chat in current_user.created_chats[:]:
        if chat['code'] == chat_code and chat['creator'] == current_user.username:
            current_user.created_chats.remove(chat) 
            all_users = load_users("users.json")

            updated_chats = []
            for chat in all_users[current_user.username]['created_chats']:
                if chat['code'] != chat_code:
                    updated_chats.append(chat)
            all_users[current_user.username]['created_chats'] = updated_chats

            save_users("users.json", all_users)

            print("Chat deleted successfully.")
            break
    else:
        print("You are not the creator of this chat or the chat code is incorrect.")


def show_created_chats():
    """Show the list of chats created by the current user."""
    if current_user.created_chats:
        print("Your created chats:")
        for chat in current_user.created_chats:
            print(f"Chat Code: {chat['code']}, Members: {chat['members']}")
    else:
        print("You have not created any chats.")


def show_joined_chats():
    """Show the list of chats joined by the current user."""
    if current_user.joined_chats:
        print("Your joined chats:")
        for chat in current_user.joined_chats:
            print(f"Chat Code: {chat['code']}, Members: {chat['members']}")
    else:
        print("You have not joined any chats.")


def chat_session(chat):
    """Handle the chat session."""
    print("A gentle reminder: you cannot finish the chat unless you enter 'finish'!")
    while True:
        chat_message = input("Enter the message: ")
        if chat_message.lower() == 'finish':
            print("You finished the chat! See you")
            break
