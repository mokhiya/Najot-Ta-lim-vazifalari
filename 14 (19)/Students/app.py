import os

def making_folder():
    user_name = input("Enter a student's name: ").title()
    
    if os.path.excists("14 (19)/Students/user_name"):
        print("This folder already excists!")
    else:
        os.mkdir("14 (19)/Students/user_name")

    return show_menu()

def adding_subject_grade(making_folder):
    student_name = input("Enter a student's name: ").title()
    subject = input("Enter a subject: ")
    grade = input("Enter a grade: ")

    if student_name == os.path.excists("14 (19)/Students/user_name"):
        new_file = open(subject + ".txt", "x")
        new_file.write(grade)
        new_file.close()
    else:
        print("You don't have a folder named with this studen't name!")
        yes_no_input = input("Would you like to create a folder? y or n >>> : ")
        if yes_no_input.lower() == "y":
            making_folder()
        else:
            show_menu()
    
def re_grading():

    name = input("Enter your student's name: ")
    subject = input("Which subject's grade do you want to change ?")
    new_grade = input("To which grade do you want to change? ")

    

def show_menu():

    menu = """
    1. Make a folder.
    2. Add a subjet and grade.
    3. Re-grade.
    4. Remove a subject.
    5. REmove a folder.
    
    """
    print(menu) 
    
    user_input = int(input("Choose an option from the menu. Press a number: "))

    if user_input == 1:
        pass
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
    elif user_input == 5:
        yes_no_input = input("Would you like to quit? (y/n): ")
        if yes_no_input.lower() == "y":
            print("You quit the program. See you!")
        else:
            show_menu()
    else:
        print("Choose a proper number! ")
        return show_menu()