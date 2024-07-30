from userclass import User, user_manager, current_user, load_users, save_users


def login_user():
    """Log in an existing user by verifying username and password."""
    global current_user
    
    user_name = input("Enter your username: ").title().strip()
    user_password = input("Enter your password: ")
    hashed_password = User.hash_password(user_password=user_password)

    all_users = load_users("users.json")
    if user_name in all_users and all_users[user_name]['password'] == hashed_password:
        current_user = User(full_name=all_users[user_name]['full_name'],
                           username=all_users[user_name]['username'],
                           password=all_users[user_name]['password'])
        current_user.is_login = True
        current_user.created_chats = [chat for chat in user_manager.read() if chat.get('creator') == user_name]
        current_user.joined_chats = [chat for chat in user_manager.read() if user_name in chat.get('members', [])]
        print("You have logged in successfully!")
        return True
    
    print("User does not exist or invalid password")
    return False


def register_user():
    """Register a new user."""
    full_name = input("Enter your full name: ").title().strip()
    user_name = input("Choose a username for yourself: ").title().strip()

    password = input("Choose any password: ")
    confirmed_password = input("Confirm your password: ")

    if password != confirmed_password:
        print("Sorry, your passwords did not match, please, start the registration again!")
        return False

    hashed_password = User.hash_password(user_password=confirmed_password)
    user_data = {
        'full_name': full_name,
        'username': user_name,
        'password': hashed_password,
        'created_chats': [],
        'joined_chats': []
    }
    user_manager.add_data(data=user_data)
    print("Congratulations, you have registered successfully!\n")
    return True
