'''
Classes: Student, Course, Teacher 
Student Variables: name, email, phone_number, id 
Methods: - register - get_info - delete_account - get_registered_courses - register_to_course 
Teacher Variables: name, phone_number, profession, age 
Methods: - add_to_file - get_info - delete_course - get_registered_users 
Course Variables: name, price, teacher 
Methods: - add_to_file - get_info - delete_course - get_registered_users 

Menu: 
1. Create a new teacher: name, phone_number, profession, age 
2. Crate a course: name, price, teacher_phone_number 
3. Register to course: name, email, phone_number, id 
4: Delete a course: name 
5: Delete a teacher: phone_number 
6: Get registered courses: phone_number 
7. Get users by course: course_name 
8. Exit
'''

import json
import os

class Student:
    def __init__(self):
        self.file_name = "data.json"

        # Create an empty data.json file if it doesn't exist
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                json.dump({}, file)

    def read_data(self):
        with open(file=self.file_name, mode='r') as file:
            data = json.load(file)
            return data

    def add_to_file(self, name, email, phone_number, student_id, teacher_data):
        student = {
            "id": student_id,
            "name": name,
            "email": email,
            "phone": phone_number,
            "teacher": teacher_data,
            "course": {}
        }
        existing_data = self.read_data()
        existing_data["students"] = existing_data.get("students", [])  # Create "students" key as a list if it doesn't exist
        existing_data["students"].append(student)  # Append the new student data

        with open(self.file_name, 'w') as file:
            json.dump(existing_data, file, indent=4)
            return "Student data has been added"

class Teacher:
    def __init__(self):
        self.file_name = "data.json"

    def add_to_student(self, student_id, full_name, phone_number, profession, age):
        teacher_data = {
            "full_name": full_name,
            "phone_number": phone_number,
            "profession": profession,
            "age": age
        }
        existing_data = self.read_data()
        students = existing_data.get("students", [])
        for student in students:
            if student["id"] == student_id:
                student["teacher"] = teacher_data
                break

        with open(self.file_name, 'w') as file:
            json.dump(existing_data, file, indent=4)
            return "Teacher data has been added to the student"

    def read_data(self):
        with open(self.file_name, 'r') as file:
            data = json.load(file)
            return data

def show_menu():
    print("Welcome to menu: ")
    menu = """
    Options:
    1. Create a new teacher.
    2. Create a course.
    3. Register for a course.
    4. Delete a course.
    5. Delete a teacher.
    6. Get registered courses.
    7. Get users by course.
    8. Exit.
    """
    print(menu)

    try:
        user_input = int(input("What would you like to do? "))
    except ValueError:
        print("Enter a number, please")
        show_menu()


    student = Student()
    teacher = Teacher()

    if user_input == 1:
        full_name = input("Enter the full name of the teacher: ")
        phone_number = input("Enter the phone number of the teacher: ")
        profession = input("What does he/she teach? ")
        age = input("Enter the age of the teacher: ")
        student_id = input("Enter the student ID: ")
        result = teacher.add_to_student(student_id, full_name, phone_number, profession, age)
        print(result)

show_menu()

