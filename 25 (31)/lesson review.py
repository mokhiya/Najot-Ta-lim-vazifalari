import hashlib, os, json

class JsonManager:
    """
    This class is applied to manage working with json files
    """
    file_name = 'products.json'


    def check_existance(self):
        """
        This method checks the existance of the file
        """
        return os.path.exists(self.file_name)


    def read_file(self):
        """
        This method reads the data of the file
        """
        if self.check_existance():
            if os.path.getsize(self.file_name) != 0:  # if the file is not empty
                with open(self.file_name, mode="r") as file:
                    data = json.load(file)
                    return data
            return []
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


class Student(JsonManager):
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password


    def registering_user():
        """
        This function is used to register users.
        """

        user_name = input("Enter your full name: ").title().strip()
        
        while True:  # Checking if user enters valid email
            user_email = input("Enter your email: ").strip()
            if user_email.endswith('@gmail.com') or user_email.endswith('@mail.ru') or user_email.endswith('@yahoo.com'):
                break
            else:
                print("Invalid input, enter an email again!")

        while True:  # Checking if user enters valid number
            phone_number = input("Enter your phone number in the format 998946718299: ")
            if len(phone_number) == 12 and phone_number.isdigit:
                break
            else:
                print("Invalid input, enter a phone number again!")
            
        while True:
            user_password = input("Enter your password: ")
            hashed_password = hashlib.sha256(user_password.encode()).hexdigest()
            user_password2 = input("Enter your password again: ")
            hashed_password2 = hashlib.sha256(user_password2.encode()).hexdigest()
            if hashed_password == hashed_password2:
                print("Your password has been saved sucessfully!")

def display_menu():
    """
    This function displays the main menu and handle user input.
    """
    menu = """
    Options:
    1. Registration.
    2. Login.
    3. Exit.
    """
    print(menu)

    user_input = int(input("Choose an option from the menu. Press a number: "))

    if user_input == 1:
        pass
    elif user_input == 2:
        pass
    elif user_input == 3:
        yes_no_input = input("Would you like to quit? (y/n): ")
        if yes_no_input.lower() == "y":
            print("You quit the program. See you!")
        else:
            return display_menu()
    else:
        print("Choose a proper number! ")
        return display_menu()
        

# Starting the program by displaying the main menu
display_menu()