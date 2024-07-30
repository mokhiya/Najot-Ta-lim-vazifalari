"""
Ovqat zakaz qilish uchun terminalda ishlaydigan dastur tuzish kerak: 
Uni quyidagi imkoniyatlari bo'lishi kerak: 

0. Oshxona va ovqatlarini qo'shish:
1. Hamma oshxonalarni ko'rish: 
2. Biror bir oshxonani nomi bo'yicha uni hamma ovqatlarini ko'rish:
3. Taom ni nomi bo'yicha qidirish:
4. Biror bir oshxonani nomi bo'yicha o'chirish: 
5. Chiqish

Pastda ma'lumotlarni qanday saqlash mumkinligi haqida ma'lumot: 

database = {
    'kfc': {
        'qanot': 12200,
        'cola': 4000,
        'suv': 3000
    },
    'oqtepa': {
        'lavash': 22000,
        'burger': 40000,
        'suv': 3000
    },
    'evos': {
        'lavash_mini': 12200,
        'sendvich': 40000,
        'suv': 3000
    },
    'loook': {
        'smilebox': 32000,
        'burger': 42000,
        'suv': 4000
    }
}
"""
# Initializing an empty dictionary to store food courts and their menus
food_courts = dict()


def adding_foodcourt():
    """
    This function adds a new food court and its menu to the dictionary.
    """
    foodcourt_name = input("Add a name of food-court: ").title()
    food_limit = int(input("How many meals do you want to add? "))

    menu = dict()
    for order in range(food_limit):
        meal = input(f"Enter the name of meal {order + 1}: ").title()
        price = float(input(f"Enter the price for {meal}: "))
        menu[meal] = price

    # Add the food court and its menu to the dictionary
    food_courts[foodcourt_name] = menu
    print("______________________________________________________")
    print(f"{foodcourt_name} has successfully been added to the list!")
    print("______________________________________________________")
    return show_menu()


def show_all_foodcourts(food_courts):
    """
    This function displays all available food courts and their menus.
    """
    print("All available food-courts: ")

    # generating each key and value of the dictionary
    for food_court, menu in food_courts.items():
        print(f"Food-court: {food_court};\t   Menu: {menu}")
    return show_menu()


def display_specific_foodcourt():
    """
    This function displays the menu for a specific food court.
    """
    specific_foodcourt_name = input("Enter a name of food-court: ").title()

    # extracting key from the dictionary
    menu = food_courts.get(specific_foodcourt_name)
    
    # if extracted key corresponds with user's input, it displays a specific foodcourt 
    if menu: 
        print(f"Menu at {specific_foodcourt_name}: {menu}")
    else:
        print(f"No such food-court named {specific_foodcourt_name}. Please re-enter the name.")
        return display_specific_foodcourt()

    return show_menu()


def display_foudcourt_by_meal():
    """
    This function searches for a specific meal across all food courts.
    """
    searched_meal = input("Please enter a meal: ").title()

    # extracting keys and values from the dictionary and checking if searched meal is in each item of the values
    for foodcourt, meals in food_courts.items():
        for meal in meals:
            if searched_meal in meal:
                print(f"{meal} is available at {foodcourt}")

    return show_menu()


def removing_foodcourt():
    """
    This function removes a food court from the dictionary.
    """
    foodcourt_name = input("Which food-court do you want to remove from the list? ")
    confirmation_message = input(f"Do you really want to remove {foodcourt_name.title()}? y or n >>> ")

    if confirmation_message.lower() == "y":
        if foodcourt_name.title() in food_courts:
            
            # Removing the specified food court
            food_courts.pop(foodcourt_name.title())
            return show_menu()
        else:
            print(f"There is no food-court called {foodcourt_name}. Please re-enter the name: ")
            return removing_foodcourt()
    else:
        return show_menu()


def show_menu():
    """
    This function displays the main menu and handles user input.
    """
    welcoming = "Welcome to a food-ordering system."
    menu = """
    Options:
    0. Adding a food-court and menu.
    1. Show all food-courts.
    2. See a specific food-court and its menu.
    3. Search by food.
    4. Delete a food-court by its name.
    5. Exit.
    """
    print(welcoming)
    print(menu)

    user_input = int(input("Choose an option from the menu. Press a number: "))

    if user_input == 0:
        adding_foodcourt()
    elif user_input == 1:
        show_all_foodcourts(food_courts)
    elif user_input == 2:
        display_specific_foodcourt()
    elif user_input == 3:
        display_foudcourt_by_meal()
    elif user_input == 4:
        removing_foodcourt()
    elif user_input == 5:
        yes_no_input = input("Would you like to quit? y or n >>> ")
        if yes_no_input.lower() == "y":
            print("You quit the program. See you!")
        else:
            show_menu()
    else:
        print("Choose a proper number! ")
        show_menu()

# Starting the program by displaying the main menu
show_menu()

