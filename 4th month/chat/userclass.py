import hashlib
from jsonmanager import JsonManager

user_manager = JsonManager(file_name="users.json")
current_user = None  

class User:
    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.is_login = False
        self.created_chats = []
        self.joined_chats = []


    def check_password(self, confirmed_password):
        """Check if the confirmed_password matches the user's password."""
        return confirmed_password == self.password


    @staticmethod
    def hash_password(user_password):
        """Hash the user's password using SHA-256."""
        return hashlib.sha256(user_password.encode()).hexdigest()


def load_users(file_name):
    """Load user data from JSON file."""
    manager = JsonManager(file_name)
    all_users = manager.read()
    users = {}
    for user in all_users:
        if 'username' in user and 'password' in user:
            users[user['username']] = user
    return users


def save_users(file_name, users):
    """Save user data to JSON file."""
    manager = JsonManager(file_name)
    manager.write(list(users.values()))

