# Online kurslar uchun ro'yxatdan o'tish dasturini tuzish kerak: 
# Unda quyidagi imkoniyatlar bo'ladi: 
# 1. Kurs qo'shish 
# 2: Barcha kurslar ro'yxatini ko'rish 
# 3. Biror kurs uchun ro'yxatdan o'tish: phone, full_name 
# 4. O'zi ro'yxatdan o'tgan kurslarni ro'yxatini ko'rish: 
# 5. Chiqish: Bitta kursga ikki martta ro'yxatdan o'tish mumkin emas. 
# Shuni hisobga olib qo'yinglar. 

course_enrollment = dict()  # A global dictionary to store course enrollment information


def adding_course():
    """
    This function adds a new course to the course enrollment dictionary.
    """
    course_name = input("Add the name of the course: ").title()

    course_info = dict()
    course_price = int(input(f"Enter the price for {course_name}: "))
    course_duration = int(input(f"Enter the duration of {course_name} in months: "))

    course_info['price'] = course_price
    course_info['duration'] = course_duration

    course_enrollment[course_name] = course_info

    print(" ")
    print(f"{course_name} has been successfully added to the list!")
    print("_" * 60)
    return show_menu()


def show_all_courses():
    """
    This function is to display all available courses and their details.
    """
    print("All available courses: ")

    if len(course_enrollment) == 0: # checking if the user entered any course beforehand
        print("No courses available.")
    else:
        print("Course\t\tPrice\t\tDuration (months)")
        print("-----------------------------------------")
        for course, info in course_enrollment.items():
            price = info['price']
            duration = info['duration']
            print(f"{course}\t\t{price}\t\t{duration}")

    return show_menu()


users_courses = []  # List to store enrolled courses of students

def enrolling_course():
    """
    This function is to enroll a student in a course.
    """
    phone_number = input("Enter your phone number in the format +998949718299: ")
    full_name = input("Enter your full name: ")

    print("Available courses:")
    for course in course_enrollment.keys():
        print(course)

    user_input = input("Which course would you like to enroll in? ").title()

    # Checking if the student is already enrolled in the same course
    for course in users_courses:
        if course['Enrolled_student'] == full_name and course['Enrolled_course'] == user_input:
            print(f"You are already enrolled in the course: {course['Enrolled_course']}")
            return show_menu()

    if user_input in course_enrollment:
        enrolled_course = {
            'Contact': phone_number,
            'Enrolled_student': full_name,
            'Enrolled_course': user_input
        }
        users_courses.append(enrolled_course)
        print(f"You have successfully enrolled in the course: {user_input}")
    else:
        print("Invalid course selection. Please choose from the available courses.")
        
        # The loop continues until a valid input is received
        # Once a valid input is received, the loop breaks and control returns to the main menu
        while True:
            user_response = input("Enter '1' to re-register or '2' to see all available courses: ")
            if user_response == '1':
                return enrolling_course()
            elif user_response == '2':
                return show_all_courses()
            else:
                print("Invalid input. Please try again.")

    return show_menu()


def display_enrolled_courses():
    """
    This function is to display the courses in which a student is enrolled.
    """
    users_name = input("Enter your full name you used for enrollment: ")

    for course in users_courses:
        if course['Enrolled_student'] == users_name:
            print("You are enrolled in:\n", course)
        else:
            print("You are not enrolled in any course.")
            return enrolling_course()


print("Welcome to the course enrollment system!") # welcoming text which appears only once in the beginning of the program


def show_menu():
    """
    This function is to display the main menu and handle user input.
    """

    menu = """
    Options:
    1. Add a course name and its price.
    2. Show all courses.
    3. Enroll in a specific course.
    4. Display enrolled courses.
    5. Exit.
    """
    print(menu)

    user_input = int(input("Choose an option from the menu. Press a number: "))

    if user_input == 1:
        adding_course()
    elif user_input == 2:
        show_all_courses()
    elif user_input == 3:
        enrolling_course()
    elif user_input == 4:
        display_enrolled_courses()
    elif user_input == 5:
        yes_no_input = input("Would you like to quit? (y/n): ")
        if yes_no_input.lower() == "y":
            print("You quit the program. See you!")
        else:
            show_menu()
    else:
        print("Choose a proper number! ")
        return show_menu()


# Starting the program by displaying the main menu
show_menu()