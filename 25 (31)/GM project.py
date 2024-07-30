import json 
import os
import hashlib

class JsonManager:
    """
    This class is applied to manage working with json files
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def check_existance(self):
        """
        This method checks the existance of the file and if the file is not empty
        """
        return os.path.exists(self.file_name) and os.path.getsize(self.file_name) != 0

    def read_file(self):
        """
        This method reads the data of the file
        """
        if self.check_existance():
                with open(self.file_name, mode="r") as file:
                    return json.load(file)
        return []
        
    def write_file(self, all_data):
        """
        This method writes all data into the file
        """
        with open(self.file_name, mode= "w") as file:
            json.dump(all_data, file, indent=4)
            return "Data is written to a file"

    def add_onedata_to_file(self, data: dict):
        """
        This method writes one given data into the the file
        """
        all_data = self.read_file()
        all_data.append(data)
        return self.write_file(all_data)
    
    def show_all_data(self):
        """
        This method is used to show a stored data
        """
        products = self.read_file()
        data_str = ""
        for product in products:
            for key, value in product.items():
                data_str += f"{key}: {value}\n"
        return f"All data:\n\n{data_str}"


file_manager = JsonManager(file_name="users.json")  # Making a global object from JsonManager class

class Users:
    """This class initializes a user with full_name, email, password, and default attributes."""
    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.is_login = False
        self.orders = []  # List to store user orders

    def check_password(self, confirmed_password):
        """This method checks if the confirmed_password matches the user's password."""
        return confirmed_password == self.password

    @staticmethod
    def hash_password(user_password):
        """This method hashes the user's password using SHA-256."""
        return hashlib.sha256(user_password.encode()).hexdigest()

current_user = None  # Global variable to store data about user that logs in.

def register_user():
    """
    This function is used to  register a user
    """
    full_name = input("Enter your full name: ").title().strip()
    
    while True:  # Checking if user enters valid email
        user_email = input("Enter your email: ").strip()
        if user_email.endswith('@gmail.com') or user_email.endswith('@mail.ru') or user_email.endswith('@yahoo.com'):
            break
        else:
            print("Invalid input, enter an email again!")

    user_password = input("Enter your password: ")
    confirm_user_password = input("Confirm your password: ")

    user = Users(full_name=full_name, email=user_email, password=user_password)
    if not user.check_password(confirmed_password=confirm_user_password):
        print("Sorry, your passwords did not match, please, start the registration again!")
        return register_user()
    else:
        user.password = Users.hash_password(user_password=user_password)
        print("Congratulations, you have registered sucessfully!\n")

        file_manager.add_onedata_to_file(data=user.__dict__)
        return display_main_menu()


def login_user():
    """This function is used to log in an existing user by verifying email and password."""
    global current_user
    
    while True:  # Checking if user enters valid email
        user_email = input("Enter your email: ").strip()
        if user_email.endswith('@gmail.com') or user_email.endswith('@mail.ru') or user_email.endswith('@yahoo.com'):
            break
        else:
            print("Invalid input, enter an email again!")

    user_password = input("Enter your password: ")
    hashed_password = Users.hash_password(user_password=user_password)

    all_users = file_manager.read_file()
    for user_data in all_users:
        if user_data['email'] == user_email and user_data['password'] == hashed_password:
            user = Users(full_name=user_data['full_name'], email=user_data['email'], password=user_data['password'])
            user.is_login = True
            current_user = user
            print("You have logged in successfully!")
            return display_user_menu(current_user)
    print("User does not exist or invalid password")
    return display_main_menu()


def logout_all_users():
    """This function is used to log out all logged-in users by updating their is_login status in the JSON file."""
    all_users = file_manager.read_file()
    index = 0
    while index < len(all_users):
        all_users[index]['is_login'] = False
        index += 1
    file_manager.write_file(all_users)
    return display_main_menu()


def display_car_options():
    print("Available cars:")
    # List of available cars
    available_cars = [
        {"name": "Toyota", "model": "Camry", "year": 2023, "price": 25000},
        {"name": "Honda", "model": "Accord", "year": 2024, "price": 45000},
        {"name": "Ford", "model": "Mustang", "year": 2022, "price": 35000}
    ]

    index = 1
    for car in available_cars:
        print(f"{index}. {car['name']} {car['model']} - {car['year']} - ${car['price']}")
        index += 1

    user_choice = int(input("Choose a car number to order: "))
    selected_car = available_cars[user_choice - 1]
    return selected_car


def order_car(selected_car, current_user):
    """This funtion is used to add an ordered car to the current user's orders and update the JSON file."""
    order_details = {
        "name": selected_car["name"],
        "model": selected_car["model"],
        "year": selected_car["year"],
        "price": selected_car["price"],
        "user_email": current_user.email
    }
        
    current_user.orders.append(order_details)
    
    all_users = file_manager.read_file()
    for user in all_users:
        if user['email'] == current_user.email:
            user['orders'] = current_user.orders
            break
    file_manager.write_file(all_users)
    print(f"You have successfully ordered a {selected_car['name']} {selected_car['model']}.")


def display_user_menu(current_user):
    """This function is used to display a menu for the logged-in user to order cars, view orders, or log out."""
    while True:
        text = """
        1. Order a car.
        2. My orders.
        3. Log out.
        """
        print(text)

        user_input = input("Choose a number from the menu: ").strip()

        if user_input == "1":
            selected_car = display_car_options()
            if current_user and current_user.is_login:
                order_car(selected_car, current_user)
            else:
                print("Please log in first to order a car.")
        elif user_input == "2":
            if current_user and current_user.is_login:
                if current_user.orders:
                    print("Your orders:")
                    index = 1
                    for order in current_user.orders:
                        print(f"{index}. {order['name']} {order['model']} - ${order['price']}")
                        index += 1
                else:
                    print("You have no orders yet.")
            else:
                print("Please log in first to view your orders.")
        elif user_input == "3":
            if current_user and current_user.is_login:
                current_user.is_login = False
                file_manager.write_file(file_manager.read_file())  # Update user status in the file
                print("You have been logged out.")
            return display_main_menu()
        else:
            print("Invalid input, please try again.")

print("Welcome to a car ordering system.")

def display_main_menu():
    """This function is used to show a main manu to a user"""
    text = """
    
    1. Register.
    2. Login.
    3. Exit. """

    print(text)

    user_input = int(input("Choose a number from menu: "))

    if user_input == 1:
        register_user()
    elif user_input == 2:
        login_user()
    elif user_input == 3:
        yes_no_input = input("Would you like to quit? (y/n): ")
        if yes_no_input.lower() == "y":
            print("You quitted the program. See you!")
        else:
            return display_main_menu()
    else:
        print("Choose a proper number! ")
        return display_main_menu()
    
if __name__ == "__main__":
    logout_all_users()