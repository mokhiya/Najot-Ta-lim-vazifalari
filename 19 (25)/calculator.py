"""
Terminalda ishlaydigan kalkulator yasash kerak, barcha najotalarni faylda
saqlab ketish kerak, va try exceptlardan foydalanish kerak,
unda quyidagi imkoniyatlari bo'lishi kerak.

Menu:
    1. 2 ta sonni qo'shish:
    2. 2 ta sonni ayirish:
    3. 2 ta sonni bo'lish:
    4. 2 ta sonni ko'paytirish
    5. Darajaga oshirish: son, daraja
    6. Barcha natijalarni ko'rish:
    7. Barcha natijalarni amal bo'yicha ko'rish: (yani odam 7 ni kiritsa siz unda qaysi amal bilan bajarilgan ishlarni
                                                ko'rmoqchi ekanligini so'raysiz u amalni kiritadi va shu amal
                                                 bilan bajarilgan ishlanri ro'yxatini ko'rsatasiz)
    8. Barcha natijalarni o'chirish:
    9. Chiqish
"""
import os

def writing_to_file(result):
    """
    This function is used to write all data into a txt file
    """
    try:
        if not os.path.exists("results.txt"):
            with open(file="results.txt", mode="w", encoding="UTF-8") as result_txt:
                result_txt.writelines(result)
                result_txt.flush()
        else:
            with open(file="results.txt", mode="a", encoding="UTF-8") as result_txt:
                result_txt.writelines(result)
                result_txt.flush()

    except Exception as e:
        print(f"Error writing to file: {e}")


def adding_numbers(number1: float, number2: float) -> str:
    """
    This function is used to add two numbers
    """
    addition_result = number1 + number2
    text_result = f"{number1} + {number2} = {addition_result}"
    print(text_result)

    writing_to_file(result=text_result)
    return display_menu()


def subtraction_numbers(number1: float, number2: float) -> str:
    """
    This function is used to substract two numbers
    """
    subtraction_result = number1 - number2
    text_result = f"{number1} - {number2} = {subtraction_result}"
    print(text_result)

    writing_to_file(result=text_result)
    return display_menu()


def dividing_numbers(number1: float, number2: float) -> str:
    """
    This function is used to divide two numbers
    """
    try:
        division_result = number1 / number2
        text_result = f"{number1} / {number2} = {division_result}"
        print(text_result)

        writing_to_file(result=text_result)
        return display_menu()

    except ZeroDivisionError:
        print("You can't divide by 0")
        return display_menu()


def multiplying_numbers(number1: float, number2: float) -> str:
    """
    This function is used to multiply two numbers
    """
    multiplication_result = number1 * number2
    text_result = f"{number1} / {number2} = {multiplication_result}"
    print(text_result)

    writing_to_file(result=text_result)
    return display_menu()

def multplying_degree(number1: float, number2: float) -> str:
    """
    This function is used to multiplying by degree
    """
    multplying_degree = number1 ** number2
    text_result = f"The {number2} degree of number {number1} is {multplying_degree}"
    print(text_result)
    
    writing_to_file(result=text_result)
    return display_menu()


def reading_all_data():
    """
    This function is used to read all data from txt file
    """
    with open(file="results.txt", mode="r", encoding="UTF-8") as txt_file:
        print("All results: \n")

        for line in txt_file:
            print(line)
    
    return display_menu()


def displaying_data_by_operation():
    """
    This function is used to display data according to e certain operation
    """
    text = input("Which operation's results do you want to see? Enter +, -, /, *, or degree >>> ")

    with open(file="results.txt", mode="r", encoding="UTF-8") as txt_file:
        found_result = False  

        if text.strip().lower() == "+":
            for line in txt_file:
                if "+" in line:
                    print(line)
                    found_result = True  

        elif text.strip().lower() == "-":
            for line in txt_file:
                if "-" in line:
                    print(line)
                    found_result = True

        elif text.strip().lower() == "/":
            for line in txt_file:
                if "/" in line:
                    print(line)
                    found_result = True

        elif text.strip().lower() == "*":
            for line in txt_file:
                if "*" in line:
                    print(line)
                    found_result = True

        elif text.strip().lower() == "degree":
            for line in txt_file:
                if "degree" in line:
                    print(line)
                    found_result = True

        else:
            print("Invalid input, try again")
            displaying_data_by_operation()

        if not found_result:
            print("No result with this operation")

    return display_menu()


def deleting_all_data():

    try:
        with open(file="results.txt", mode="w", encoding="UTF-8") as txt_file:
            txt_file.truncate(0)
        print("All data has been deleted from the file.")
    except Exception as e:
        print(f"Error deleting data: {e}")

    return display_menu()

def display_menu():
    """
    This function displays the main menu and handle user input.
    """
    menu = """
    Options:
    1. Addition.
    2. Subtraction.
    3. Division.
    4. Multiplication.
    5. Multiplying by degree.
    6. Removing all data.
    7. Displying results by operation.
    8. Deleting all data.
    9. Exit.
    """
    print(menu)

    user_input = int(input("Choose an option from the menu. Press a number: "))
    if user_input in [1, 2, 3, 4]:
        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid value. Enter a number")

    if user_input == 1:
        adding_numbers(first_number, second_number)
    elif user_input == 2:
        subtraction_numbers(first_number, second_number)
    elif user_input == 3:
        dividing_numbers(first_number, second_number)
    elif user_input == 4:
       multplying_degree(first_number, second_number)
    elif user_input == 5:
        multiplying_numbers()
    elif user_input == 6:
        reading_all_data()
    elif user_input == 7:
        displaying_data_by_operation()
    elif user_input == 8:
        yes_no_input = input("Warning, you may delete all data, are you sure? (y/n): ")
        if yes_no_input.lower() == "y":
            deleting_all_data()
        else:
            return display_menu()
    elif user_input == 9:
        yes_no_input = input("Would you like to quit? (y/n): ")
        if yes_no_input.lower() == "y":
            print("You quit the program. See you!")
        else:
            return display_menu()
    else:
        print("Choose a proper number! ")
        return display_menu()
        

# Starting the program by displaying the main menu
if __name__=="__main__":
    display_menu()

