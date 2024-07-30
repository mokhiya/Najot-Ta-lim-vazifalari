import hashlib

class Renter():
    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.is_login = False
        self.rented_houses = []  # List to store houses the renter has got interested

    def check_password(self, confirmed_password):
        """This method checks if the confirmed_password matches the user's password."""
        return confirmed_password == self.password

    @staticmethod
    def hash_password(user_password):
        """This method hashes the user's password using SHA-256."""
        return hashlib.sha256(user_password.encode()).hexdigest()

    def add_house(self, house):
        """Add a book to the user's list of read books."""
        self.posted_houses.append(house)
        return "House has been added to your posted_houses list!"