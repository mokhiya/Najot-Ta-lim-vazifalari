your_contacts = dict()

def add_contact():

    contact_name = input("Enter a name of your contact: ")
    if contact_name in your_contacts.keys():
        print("This contact name already excists. Please, rename your contact name: ")
        return add_contact
    else:
        number = int(input("enter your contac's number: "))

        your_contacts[contact_name] = number
        return show_menu()

def show_menu():
    text = """
    1. Add a new contact and number.
    2. Search for name.
    3. Update a number.
    4. Delete a contat.
    5. Show all contacts.
    6. Exit.
    """

    print(text)

    user_input = int(input("Choose a number from menu: "))
    if user_input == 1:
        add_contact()
    elif user_input == 5:
        pass
    elif user_input == 6:
        print("Goodbye")
        return

show_menu()