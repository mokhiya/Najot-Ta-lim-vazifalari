
student = dict()
subjects = ["Math", "Physics", "Music"]

for i in range(3):
    student_name = input("Enter a student's name: ")
    grade = input(f"Enter your grade for {subjects[i]}: ")
    student[student_name] = grade

print(student)

