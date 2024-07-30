import os

for _ in range(5):
    
    subject_name = input("Enter a subjet name: ")

    if os.path.exists(subject_name + ".txt"):
        print("You have already created this file!")
    else:
        new_file = open(subject_name + ".txt", "x")
        text = input("Enter a grade: ")
        new_file.write(text)
        new_file.close()
