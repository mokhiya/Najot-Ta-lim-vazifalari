""" Foydalanuvchini shaxsiy ma'lutlarini saqlash uchun programma yasash kerak. 
Qanday faylda sqlash kerakligini ham foydalanuvchi tanlaydi. 
Menu: 
1: Save personal data: name, email, file_type(csv, json, txt) 
2: Read personal data: email 
3: Delete personal data: email 
4: Exit 
Hohlasangiz har bitta foydanuvchini malumoti uchun alohida fayl ochishingiz mumkin. 
Yoki barcha foydalanuvchilar uchun 
3 ta turgani csv, txt, json turdagi fayl ochib shuni ichiga saqlab ketsangiz ham bo'ladi. 
Barcha malumotlar bitta users nomli papkani ichida bo'lishi kerak. 
Papka mavjud yoki mavjud emasligini tekshirib olish va yo'q bo'lsa yaratib qo'ying. """



import os
import json
import csv

folder_path = './users'  # Creating a folder path to use it later

# Checking if the folder exists, if no, it creates a folder
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print(f"Folder '{folder_path}' created successfully.")
else:
    print(f"Folder '{folder_path}' already exists.")


def registering_user():
    """
    This function is used to store a user data
    """
    user_name = input("Enter your full name: ").title().strip()
    user_email = input("Enter your email: ").strip()
    user_data = [user_name, user_email]
    saving_data(user_data)

def saving_data(data):
    """
    This function is used to save a user data into various types of files according to user's preference
    """

    user_name, user_email = data

    options = int(input("Which type of file do you prefer to store your data?\n1.csv file.\n2.json file.\n3.txt file\nChoose a number:  "))

    # Saving data in csv file
    if options == 1:
        csv_file_path = folder_path + "./csv_data.csv"
        with open(file=csv_file_path, mode="a", encoding="UTF-8", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            if os.path.getsize(csv_file_path) == 0:
                csv_writer.writerow(["User name", "User email"])
            csv_writer.writerow([user_name, user_email])
            print(f"CSV file '{csv_file.name}' created, and your data has been saved successfully.")

    # Saving data in json file
    elif options == 2:
        if os.path.exists(folder_path + "./json_data.json"):
            with open(file=folder_path + "./json_data.json", mode="r", encoding="UTF-8") as json_file:
                data = json.load(json_file)
        else:
            data = {}
       
        data[user_name]= {
            'User name': user_name, 
            'User email': user_email
            }
        with open(file=folder_path + "./json_data.json", mode="w", encoding="UTF-8") as json_file:
            json.dump(data, json_file, indent=4)
            print(f"JSON file '{json_file.name}' created and your data has been saved successfully.")

    # Saving data in txt file
    elif options == 3:
        data = f"User name: {user_name}, User email: {user_email}\n"
        with open(file=folder_path + "./txt_data.txt", mode="a", encoding="UTF-8") as txt_file:
            txt_file.write(data)
            print(f"Text file '{txt_file.name}' created and your data has been saved successfully.")

    else:
        option = int(input("Invalid input. What do you want to do? \n1. Create a folder again.\n2. Go to main menu.\n>>> "))
        if option == 1:
            return saving_data(data)
        else:
            return display_menu()

    return display_menu()


def reading_data():
    """
    This fuction is used to get user's data according to his email
    """
    check_email = input("Enter your email: ")

    found = False

    # Checking CSV file
    with open(file=folder_path + "./csv_data.csv", mode="r", encoding="UTF-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skipping the header row
        
        for row in csv_reader:
            if len(row) >= 2 and row[1] == check_email:
                print(f"User name: {row[0]}\nUser email: {row[1]}")
                found = True
                break

    # Checking the JSON file
    with open(file=folder_path + "./json_data.json", mode="r", encoding="UTF-8") as json_file:
        data = json.load(json_file)
        
        for username, user_data in data.items():
            if user_data.get("User email") == check_email:
                print(f"User name: {user_data.get('User name')}\nUser email: {user_data.get('User email')}")
                found = True
                break

    # Checking TXT file
    with open(file=folder_path + "./txt_data.txt", mode="r", encoding="UTF-8") as txt_file:
        for line in txt_file:
            
            if 'User email:' in line and check_email in line:
                name = line.split(',')[0].split(':')[1].strip()
                email = line.split(',')[1].split(':')[1].strip()
                print(f"User name: {name}\nUser email: {email}")
                found = True
                break

    if not found:
        print(f"No user data found for email: {check_email}")
        option = int(input("Invalid input. What do you want to do? \n1. Enter an email again.\n2. Go to main menu.\n>>> "))
        if option == 1:
            return reading_data()
        else:
            return display_menu()

    return display_menu()


def deleting_user_data():
    """
    This function deletes a user's data from the CSV, JSON, and TXT files based on their email.
    """ 

    email = input("Enter a user's email: ")
    
    # Deleting from CSV file
    rows_to_keep = []
    with open(file=folder_path + "./csv_data.csv", mode="r", encoding="UTF-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skipping the header row

        for row in csv_reader:
            if len(row) >= 2 and row[1] != email:
                rows_to_keep.append(row)

    with open(file=folder_path + "./csv_data.csv", mode="w", newline="", encoding="UTF-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Name", "Email"])  # Writing the header row again
        csv_writer.writerows(rows_to_keep)
    
    # Deleting from JSON file
    with open(file=folder_path + "./json_data.json", mode="r", encoding="UTF-8") as json_file:
        data = json.load(json_file)

    for user_id, user_data in list(data.items()):
        if user_data.get("User email") == email:
            del data[user_id]

    with open(file=folder_path + "./json_data.json", mode="w", encoding="UTF-8") as json_file:
        json.dump(data, json_file, indent=4)
    
    # Deleting from TXT file
    lines_to_keep = []
    with open(file=folder_path + "./txt_data.txt", mode="r", encoding="UTF-8") as txt_file:
        lines = txt_file.readlines()
        
        for line in lines:
            if line.strip():
                parts = line.strip().split(":")
                if len(parts) == 2:
                    email_from_file = parts[1].strip(" User email: ")
                    if email_from_file != email:
                        lines_to_keep.append(line)
    
    with open(file=folder_path + "./txt_data.txt", mode="w", encoding="UTF-8") as txt_file:
        txt_file.writelines(lines_to_keep)
    
    print(f"User data for email '{email}' has been deleted.")

    return display_menu()

def display_menu():
    """
    This function displays the main menu and handle user input.
    """
    menu = """
    Options:
    1. Save personal data.
    2. Read personal data.
    3. Delete personal data.
    4. Exit.
    """
    print(menu)

    user_input = int(input("Choose an option from the menu. Press a number: "))

    if user_input == 1:
        registering_user()
    elif user_input == 2:
        reading_data()
    elif user_input == 3:
        deleting_user_data()
    elif user_input == 4:
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