""" employess =
 { 'id': 
    { 'full_name': 'palonchi pistonchi', 
    'phone_number: '9999999999', 
    'salary': 100000, 
    'position': 'Senior Developer' } 
    } 
    
    1. yangi ishchi qo'shish 
    2. Hamma ishchilarni ko'rish 
    3. Ismi bo'yicha ishchini qidirish 
    4. Id bo'yicha ishchini o'chirish 
    5. Exit """ 
 
 # Ishchilarni malumotlarni boshqarish uchun kichik bir programma yasash kerak, 
 # unda tepadagi funksiyalar bo'lishi shart.


# Initializing an empty dictionary to store employee data
employees = dict()

def adding_new_employee():
    """
    This function adds a new employee to the 'employees' dictionary according to some parametres.
    """
    employee_id = int(input("Enter an ID number for your employee: "))

    if employee_id in employees.keys():
        print("This ID is already registered. Please, re-enter your ID: ")
        return adding_new_employee()
    else:
        employee_fullname = input("Enter a full name of your employee: ")
        phone_number = int(input("Enter a phone number of your employee in the format of '999999999': "))
        employee_salary = float(input("Enter a salary: "))
        employee_job_position = input("Enter a job position of your employee: ")

        # Adding employee data to the dictionary
        employees[employee_id] = {
            "Full name" : employee_fullname,
            "Phone number" : phone_number,
            "Salary" : employee_salary,
            "Position" : employee_job_position
        }

        print("""
        ____________________________________
        Your data has sucessfully been added!
        """)
        return show_menu()


def show_all_employee():
    """
    This function displays information for all employees in the 'employees' dictionary.
    """
    print("All information about employees: ")

    for employee in employees.items():
        show_employee = f"{employee[0]} : \t{employee[1]}"
        print(show_employee)
    
    return show_menu()

 
def check_employee(employee_name: str) -> bool:
    """
    This function checks if an employee with the given name exists.
    """
    # Checking if employees name excists in the disctionary
    if employee_name in employees.keys():
        return True
    return False


def check_employee_by_name():
    """
    This function searches for an employee by their full name.
    """
    searched_name = input("Enter a full name of an employee: ")
    print("All information about searched employees: ")

    for employee_value in employees.values():
           
        if employee_value["Full name"] == searched_name: # checking if the value in the dictionary matches with a given name
            print(employee_value)
            return show_menu()
    else:
        print("No employee with such kind of name")
        return check_employee_by_name()


def remove_employee_by_id():
    """
    This function removes an employee from the 'employees' dictionary based on their ID.
    """
    employee_id = input("Enter an employee ID: ")

    if employee_id in employees:
        employees.pop(employee_id) # removing all data of employee corresponding to his id as
        return show_menu()
    else:
        print("No employee with such an ID")
        return remove_employee_by_id()


def show_menu():
    """
    This function displays the menu options and handles user input.
    """

    menu_text = '''
    Menu bar:
    1. Add a new employee.
    2. Show all employees.
    3. Search by name.
    4. Delete by an id.
    5. exit.
    '''
    print(menu_text)
    user_input = int(input("Choose a number from menu: "))

    if user_input == 1:
        adding_new_employee()
    elif user_input == 2:
        show_all_employee()
    elif user_input == 3:
        check_employee_by_name()
    elif user_input == 4:
        remove_employee_by_id()
    elif user_input == 5:
        print("You quitted the program. See you!")


# Starting the program by displaying the menu
show_menu()