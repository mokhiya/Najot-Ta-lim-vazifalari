import hashlib
from file_managing import student_manager, product_manager

admin_id = "00"
admin_password = "00"


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = quantity


class Student:
    def __init__(self, full_name, student_id, student_password):
        self.full_name = full_name
        self.student_id = student_id
        self.student_password = student_password
        self.is_login = False
        self.coin = 100

    def check_password(self, confirm_password):
        return confirm_password == self.student_password

    @staticmethod
    def hash_password(student_password):
        return hashlib.sha256(student_password.encode()).hexdigest()


def register():
    full_name = input("Enter full name: ")
    student_id = input("Enter student id: ")
    student_password = input("Enter your password: ")
    confirm_password = input("Enter your confirm password: ")

    student = Student(full_name, student_id, student_password)
    if not student.check_password(confirm_password):
        print("Passwords do not match")
        return register()

    student.student_password = Student.hash_password(student_password)
    student_manager.add_data(data=student.__dict__)
    return show_auth_menu()


def login():
    student_id = input("Enter student id: ")
    student_password = input("Enter your password: ")
    if student_id == admin_id and student_password == admin_password:
        return show_admin_menu()
    hashed_password = Student.hash_password(student_password)

    all_users = student_manager.read()

    index = 0
    while index < len(all_users):
        if all_users[index]['student_id'] == student_id and all_users[index]['student_password'] == hashed_password:
            all_users[index]['is_login'] = True
            student_manager.write(all_users)
            return show_menu()
        index += 1
    student_manager.write(all_users)
    print("User not found, or password is incorrect")
    return show_auth_menu()


def logout_all():
    all_users = student_manager.read()
    index = 0
    while index < len(all_users):
        all_users[index]['is_login'] = False
        index += 1
    student_manager.write(all_users)
    return show_auth_menu()


def add_product():
    name = input("Enter product name: ")
    price = int(input("Enter product price in coin: "))
    quantity = int(input("enter product quantity: "))
    product = Product(name, price, quantity)

    product_manager.add_data(product.__dict__)
    print('Product added successfully!')
    return show_admin_menu()


def delete_product():
    name = input("Enter product name: ").strip()
    all_products = product_manager.read()
    new_products = []
    for product in all_products:
        if product['name'].lower() != name.lower():
            new_products.append(product)
    product_manager.write(new_products)
    print('Product deleted successfully!')
    return show_admin_menu()


####################################################################################################
def available_products():
    products = product_manager.read()

    for product in products:
        print(product)

# def buy_product():
#     products = product_manager.read()
#     name = input("Enter product name: ")

    
#     for product in products:
#         if product['name'] == name:
#             quantity = int(input(f"How many {product['name']} do you want to buy? >>> ")).strip()
#             total_quantity = product['price'] * quantity
#             if student.is_login = True and 
#             if student.coin >= total_quantity:
#                 print("You have sucesfully bought the product")
#         else:
#             print("there is no such product")

            

    # uni coini yetadimi
    # orders.json, student_id, product_name, quantity, when
    
    
def show_admin_menu():
    text = """
        1. Add product: 
        2. Delete product: 
        3. Logout: 
    """
    print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        add_product()
    elif user_input == "2":
        delete_product()


def show_menu():
    text = """
    1. Buy product: 
    2. My orders: 
    3. Logout: 
"""
    print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        pass
    else:
        print("Good bye !")
        return


def show_auth_menu():
    text = """
    1. Register
    2. Login
    3. Exit
"""
    print(text)


    user_input = input("Enter your choice: ")
    if user_input == "1":
        register()
    elif user_input == "2":
        login()
    else:
        print("Good bye !")
        return

if __name__ == "__main__":
    logout_all()
