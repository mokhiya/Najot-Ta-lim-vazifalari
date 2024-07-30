from owners import Owner
from renters import Renter
from jsonmanager import renter_manager, owner_manager


def register_renter():
    full_name = input("Enter your full name: ").title().strip()
    
    while True:
        renter_email = input("Enter your email: ").strip()
        if renter_email.endswith('@gmail.com') or renter_email.endswith('@mail.ru') or renter_email.endswith('@yahoo.com'):
            break
        else:
            print("Invalid input, enter an email again!")

    renter_password = input("Enter your password: ")
    confirm_renter_password = input("Confirm your password: ")

    renter = Renter(full_name=full_name, email=renter_email, password=renter_password)
    if not renter.check_password(confirmed_password=confirm_renter_password):
        print("Sorry, your passwords did not match, please, start the registration again!")
        return register_renter()  # Corrected function call
    else:
        renter.password = Renter.hash_password(user_password=renter_password)
        print("Congratulations, you have registered successfully!\n")

        renter_manager.add_data(data=renter.__dict__) 
        return display_renter_register_menu()


def login_renter():
    """Log in an existing renter by verifying email and password."""
    global current_renter
    
    while True:
        renter_email = input("Enter your email: ").strip()
        if renter_email.endswith('@gmail.com') or renter_email.endswith('@mail.ru') or renter_email.endswith('@yahoo.com'):
            break
        else:
            print("Invalid input, enter an email again!")

    renter_password = input("Enter your password: ")
    hashed_password = Renter.hash_password(user_password=renter_password)

    all_renters = renter_manager.read()
    for renter_data in all_renters:
        if renter_data['email'] == renter_email and renter_data['password'] == hashed_password:
            current_renter = Renter(full_name=renter_data['full_name'], email=renter_data['email'], password=renter_data['password'])
            current_renter.is_login = True
            print("You have logged in successfully!")
            return display_renter_menu()
    
    print("User does not exist or invalid password")
    return display_renter_register_menu()


def add_comment():
    if not current_renter.is_login:
        print("You must be logged in to add a comment.")
        return display_renter_register_menu()

def display_already_posted_houses():
    all_owners = owner_manager.read()
    if not all_owners:
        print("No houses are currently posted.")
        return display_renter_menu()
    
    index = 1
    for owner_data in all_owners:
        for house in owner_data.get('posted_houses', []):
            print(f"House number {index}:")
            for key, value in house.items():
                print(f"{key}: {value}")
            print("____________________")
            index += 1

    house_choice = input("Would you like to rent any of these houses? (Enter house name or 'no'): ").title().strip()
    if house_choice.lower() == 'no':
        return display_renter_menu()

    house_found = False
    for owner_data in all_owners:
        for house in owner_data.get('posted_houses', []):
            if house['house_name'] == house_choice:
                house_found = True
                current_renter.rented_houses.append(house)
                comment = input(f"Enter your comment for {house_choice}: ")
                house.setdefault('comments', []).append({
                        'renter_email': current_renter.email,
                        'comment': comment
                    })
                print(f"You have rented the house '{house_choice}' successfully.")
                
                owner_index = owner_manager.find_user_index_by_email(owner_data['email'])
                if owner_index is not None:
                    all_owners[owner_index]['posted_houses'] = owner_data['posted_houses']
                    owner_manager.update_data(owner_index, owner_data)
                break
        
        if house_found:
            break

    return display_renter_menu()


def search_house_by_rooms():
    rooms = input("Enter the number of rooms you are looking for: ").strip()
    found = False
    
    all_owners = owner_manager.read()
    for owner_data in all_owners:
        for house in owner_data.get('posted_houses', []):
            if house['house_rooms'] == rooms:
                print(f"""
House Name: {house['house_name']}
Address: {house['house_address']}
Location: {house['house_location']}
Rooms: {house['house_rooms']}""")
                print("____________________")
                found = True
    
    if found:
        house_choice = input("Would you like to rent any of these houses? (Enter house name or 'no'): ").title().strip()
        if house_choice.lower() == 'no':
            return display_renter_menu()

        house_found = False
        for owner_data in all_owners:
            for house in owner_data.get('posted_houses', []):
                if house['house_name'] == house_choice:
                    house_found = True

                    current_renter.rented_houses.append(house)
                    
                    comment = input(f"Enter your comment for '{house_choice}': ")
                    house.setdefault('comments', []).append({
                        'renter_email': current_renter.email,
                        'comment': comment
                    })
                    print(f"You have rented the house '{house_choice}' successfully.")
                    
                    owner_index = owner_manager.find_user_index_by_email(owner_data['email'])
                    if owner_index is not None:
                        all_owners[owner_index]['posted_houses'] = owner_data['posted_houses']
                        owner_manager.update_data(owner_index, owner_data)
                    break
            if house_found:
                break

        if not house_found:
            print("No house found with that name.")
    else:
        print("No houses found with that number of rooms.")

    return display_renter_menu()


def search_house_by_location():
    all_owners = owner_manager.read()
    locations = set()
    for owner in all_owners:
        if 'house_location' in owner:  
            locations.add(owner['house_location'])
    
    if not locations:
        print("No houses are available.")
        return display_renter_menu()
    else:
        index = 1
        print(f"Available locations:\n {index}.{locations}")
        index += 1

    while True:
        try:
            choice = int(input("Choose a location by number: "))
            if 1 <= choice <= len(locations):
                chosen_location = sorted(locations)[choice - 1]
                break
            else:
                print(f"Please choose a number between 1 and {len(locations)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    houses_in_location = [owner for owner in all_owners if owner['house_location'] == chosen_location]

    if not houses_in_location:
        print(f"No houses are available in {chosen_location}.")
        return display_renter_menu()

    print(f"Houses in {chosen_location}:")
    for house in chosen_location:
        for key, value in house.items():
            if key != 'comments':
                print(f"{key}: {value}")
        print("____________________")
    
    while True:
        try:
            house_choice = int(input(f"Choose a house to rent by number (1-{len(houses_in_location)}), or 0 to go back: "))
            if 0 <= house_choice <= len(houses_in_location):
                if house_choice == 0:
                    return display_renter_menu()
                else:
                    selected_house = houses_in_location[house_choice - 1]
                    rented_houses(selected_house)
                    break
            else:
                print(f"Please choose a number between 0 and {len(houses_in_location)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def rented_houses(selected_house, current_renter, owner_manager):
    if not current_renter.is_login:
        print("You must be logged in to add a comment.")
        return display_renter_register_menu()

    if selected_house is None:
        print("No house selected.")
        return display_renter_menu()

    current_renter.rented_houses.append(selected_house)
    comment = input(f"Enter your comment for '{selected_house['house_name']}': ")
    selected_house.setdefault('comments', []).append({
        'renter_email': current_renter.email,
        'comment': comment
    })
    print(f"You have rented the house '{selected_house['house_name']}' successfully.")
    
    all_owners = owner_manager.read()
    for owner_data in all_owners:
        for house in owner_data.get('posted_houses', []):
            if house['house_name'] == selected_house['house_name']:
                owner_index = owner_manager.find_user_index_by_email(owner_data['email'])
                if owner_index is not None:
                    owner_manager.update_data(owner_index, owner_data)
                break

    return display_renter_menu()


def display_renter_menu():
    text = """
    1. See all posted houses by the owner.
    2. Search house by room quantity.
    3. Search house by location.
    4. My rented houses.
    5. Logout.
    6. Go to back. """

    print(text)

    user_input = input("Choose a number from the menu: ")

    if user_input == "1":
        display_already_posted_houses()
    elif user_input == "2":
        search_house_by_rooms()
    elif user_input == "3":
        search_house_by_location()
    elif user_input == "4":
        selected_house = None
        if selected_house:
            rented_houses(selected_house, current_renter, owner_manager)
        else:
            print("No house selected. Returning to menu.")
            return display_renter_menu()
    elif user_input == "5":
        current_renter.is_login = False
        print("You have logged out successfully.")
        return display_renter_register_menu()
    elif user_input == "6":
        yes_no_input = input("Would you like to go back? (y/n): ")
        if yes_no_input.lower() == "y":
            return display_renter_register_menu()
        else:
            return display_renter_menu()
    else:
        print("Choose a proper number! ")
        return display_renter_menu()


def display_renter_register_menu():
    text = """
    House renter's menu:

    1. Register.
    2. Login.
    3. Go to back. """

    print(text)

    user_input = input("Choose a number from the menu: ")

    if user_input == "1":
        register_renter()
    elif user_input == "2":
        login_renter()
    elif user_input == "3":
        yes_no_input = input("Would you like to go back? (y/n): ")
        if yes_no_input.lower() == "y":
            display_main_menu()
        else:
            return display_renter_register_menu()
    else:
        print("Choose a proper number! ")
        return display_renter_register_menu()

#################################################################
def login_owner():
    """Log in an existing owner by verifying email and password."""
    global current_owner
    
    while True:
        owner_email = input("Enter your email: ").strip()
        if owner_email.endswith('@gmail.com') or owner_email.endswith('@mail.ru') or owner_email.endswith('@yahoo.com'):
            break
        else:
            print("Invalid input, enter an email again!")

    owner_password = input("Enter your password: ")
    hashed_password = Owner.hash_password(user_password=owner_password)

    all_owners = owner_manager.read()
    for owner_data in all_owners:
        if owner_data['email'] == owner_email and owner_data['password'] == hashed_password:
            current_owner = Owner(full_name=owner_data['full_name'], email=owner_data['email'], password=owner_data['password'])
            current_owner.is_login = True
            current_owner.posted_houses = owner_data.get('posted_houses', [])
            print("You have logged in successfully!")
            return display_owner_menu()
    
    print("User does not exist or invalid password")
    return display_owner_register_menu()


def register_owner():
    full_name = input("Enter your full name: ").title().strip()
    
    while True:
        user_email = input("Enter your email: ").strip()
        if user_email.endswith('@gmail.com') or user_email.endswith('@mail.ru') or user_email.endswith('@yahoo.com'):
            break
        else:
            print("Invalid input, enter an email again!")

    user_password = input("Enter your password: ")
    confirm_user_password = input("Confirm your password: ")

    owner = Owner(full_name=full_name, email=user_email, password=user_password)
    if not owner.check_password(confirmed_password=confirm_user_password):
        print("Sorry, your passwords did not match, please, start the registration again!")
        return register_owner() 
    else:
        owner.password = Owner.hash_password(user_password=user_password)
        print("Congratulations, you have registered successfully!\n")

        owner_manager.add_data(data=owner.__dict__)
        return display_owner_register_menu()


def post_house_info():
    """
    Collects house information from the user and posts it to the logged-in owner's list of posted houses.
    """
    if not current_owner.is_login:
        print("You must be logged in to post a house.")
        return
    
    house_name = input("How should people call your house? ").title().strip()
    house_rooms = input("How many rooms do you want to give for renting? Enter available room numbers: ")
    house_address = input("Enter your house's address: ").title().strip()
    house_location = input("In which city is your house located? ").title().strip()

    info = {
        'house_name': house_name,
        'house_rooms': house_rooms,
        'house_address': house_address,
        'house_location': house_location
    }

    current_owner.add_house(info)
    
    all_owners = owner_manager.read()
    owner_index = owner_manager.find_user_index_by_email(current_owner.email)
    if owner_index is not None:
        all_owners[owner_index]['posted_houses'] = current_owner.posted_houses
        owner_manager.update_data(owner_index, all_owners[owner_index])
        print("House information has been posted successfully.")
        return display_owner_menu()
    else:
        print("Owner data not found.")
        return display_owner_register_menu()


def display_posted_houses():
    if not current_owner.is_login:
        print("Sorry, you must first log in to see all posted houses by you!")
        return display_owner_register_menu()

    if not current_owner.posted_houses:
        print("You haven't posted any info about houses for renting")
        return display_owner_menu()
    else:
        index = 1
        for house in current_owner.posted_houses:
            print(f"House number {index}:")
            for key, value in house.items():
                print(f"{key}: {value}")
            print("____________________")
            index += 1
        return display_owner_menu()


def delete_posted_house():
    if not current_owner.is_login:
        print("Sorry, you must first log in to delete a posted house.")
        return display_owner_register_menu()

    if not current_owner.posted_houses:
        print("You haven't posted any info about houses for renting.")
        return display_owner_menu()
    else:
        house_name_to_delete = input("Enter the house name to delete it from the list: ").title().strip()
        
        house_to_delete = None
        for house in current_owner.posted_houses:
            if house['house_name'] == house_name_to_delete:
                house_to_delete = house
                break
        
        if house_to_delete is None:
            print("There is no house with this name in your posted houses.")
            return display_owner_menu()
        else:
            current_owner.posted_houses.remove(house_to_delete)
            print(f"House '{house_name_to_delete}' has been deleted successfully.")
            
            all_owners = owner_manager.read()
            owner_index = owner_manager.find_user_index_by_email(current_owner.email)
            if owner_index is not None:
                all_owners[owner_index]['posted_houses'] = current_owner.posted_houses
                owner_manager.update_data(owner_index, all_owners[owner_index])
            else:
                print("Owner data not found.")
            
            return display_owner_menu()


def see_all_interested_renters():
    global current_owner
    
    if not current_owner.is_login:
        print("You must be logged in to see all interested renters.")
        return display_owner_register_menu()
    
    if not current_owner.posted_houses:
        print("You haven't posted any houses yet.")
        return display_owner_menu()
    
    for house in current_owner.posted_houses:
        print(f"House: {house['house_name']}")
        if 'comments' in house and house['comments']:
            print("Interested Renters:")
            for comment in house['comments']:
                renter_email = comment['renter_email']
                renter_comment = comment['comment']
                print(f"Renter Email: {renter_email} - Comment: {renter_comment}")
        else:
            print("No renters have shown interest yet.")
        print("____________________")
    
    return display_owner_menu()


def display_owner_menu():
    text = """
    1. Post information about house.
    2. See all posted houses by the owner.
    3. Delete a posted house.
    4. See all interested renters.
    5. Logout.
    6. Go to back. """

    print(text)

    user_input = input("Choose a number from the menu: ")

    if user_input == "1":
        post_house_info()
    elif user_input == "2":
        display_posted_houses()
    elif user_input == "3":
        delete_posted_house()
    elif user_input == "4":
        see_all_interested_renters()
    elif user_input == "5":
        current_owner.is_login = False
        print("You have logged out successfully.")
        return display_owner_register_menu()
    elif user_input == "6":
        yes_no_input = input("Would you like to go back? (y/n): ")
        if yes_no_input.lower() == "y":
            return display_owner_register_menu()
        else:
            return display_owner_menu()
    else:
        print("Choose a proper number! ")
        return display_owner_menu()


def rent_house(house):
    """
    Handles the renting of a house including adding it to the renter's rented houses and adding a comment.
    """
    global current_renter

    while True:
        rent_choice = input(f"Do you want to rent the house '{house['house_name']}'? (y/n): ").strip().lower()
        if rent_choice in ('y', 'n'):
            if rent_choice == 'y':
                current_renter.rented_houses.append(house)
                comment = input(f"Enter your comment for the house '{house['house_name']}': ").strip()
                house.setdefault('comments', []).append({
                    'renter_email': current_renter.email,
                    'comment': comment
                })
                update_owner_data(house)  
                print(f"You have rented the house '{house['house_name']}' and added a comment.")
            else:
                print("You have chosen not to rent this house.")
            return display_renter_menu()
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def update_owner_data(rented_house):
    """
    Updates the owner's data with the new comment added to a rented house.
    """
    global owner_manager
    
    all_owners = owner_manager.read()
    for owner in all_owners:
        for house in owner.get('posted_houses', []):
            if house['house_name'] == rented_house['house_name'] and house['house_location'] == rented_house['house_location']:
                house.update(rented_house)  
                owner_index = owner_manager.find_user_index_by_email(owner['email'])
                if owner_index is not None:
                    all_owners[owner_index]['posted_houses'] = owner.get('posted_houses', [])
                    owner_manager.update_data(owner_index, owner)
                break

    owner_manager.write(all_owners) 

def display_owner_menu():
    text = """
    1. Post information about house.
    2. See all posted houses by the owner.
    3. Delete a posted house.
    4. See all interested renters.
    5. Logout.
    6. Go to back. """

    print(text)

    user_input = input("Choose a number from the menu: ")

    if user_input == "1":
        post_house_info()
    elif user_input == "2":
        display_posted_houses()
    elif user_input == "3":
        delete_posted_house()
    elif user_input == "4":
        see_all_interested_renters()
    elif user_input == "5":
        current_owner.is_login = False
        print("You have logged out successfully.")
        return display_owner_register_menu()
    elif user_input == "6":
        yes_no_input = input("Would you like to go back? (y/n): ")
        if yes_no_input.lower() == "y":
            return display_owner_register_menu()
        else:
            return display_owner_menu()
    else:
        print("Choose a proper number! ")
        return display_owner_menu()

def see_all_interested_renters():
    """
    Displays all interested renters for each house posted by the owner.
    """
    global current_owner
    
    if not current_owner.is_login:
        print("You must be logged in to see all interested renters.")
        return display_owner_register_menu()
    
    if not current_owner.posted_houses:
        print("You haven't posted any houses yet.")
        return display_owner_menu()
    
    for house in current_owner.posted_houses:
        print(f"House: {house['house_name']}")
        if 'comments' in house and house['comments']:
            print("Interested Renters:")
            for comment in house['comments']:
                renter_email = comment['renter_email']
                renter_comment = comment['comment']
                print(f"Renter Email: {renter_email} - Comment: {renter_comment}")
        else:
            print("No renters have shown interest yet.")
        print("____________________")
    
    return display_owner_menu()

def display_owner_menu():
    text = """
    1. Post information about house.
    2. See all posted houses by the owner.
    3. Delete a posted house.
    4. See all interested renters.
    5. Logout.
    6. Go to back. """

    print(text)

    user_input = input("Choose a number from the menu: ")

    if user_input == "1":
        post_house_info()
    elif user_input == "2":
        display_posted_houses()
    elif user_input == "3":
        delete_posted_house()
    elif user_input == "4":
        see_all_interested_renters()
    elif user_input == "5":
        current_owner.is_login = False
        print("You have logged out successfully.")
        return display_owner_register_menu()
    elif user_input == "6":
        yes_no_input = input("Would you like to go back? (y/n): ")
        if yes_no_input.lower() == "y":
            return display_owner_register_menu()
        else:
            return display_owner_menu()
    else:
        print("Choose a proper number! ")
        return display_owner_menu()

def display_owner_register_menu():
    text = """
    House owner's menu:

    1. Register.
    2. Login.
    3. Exit. """

    print(text)

    user_input = input("Choose a number from menu: ")

    if user_input == "1":
        register_owner()
    elif user_input == "2":
        login_owner()
    elif user_input == "3":
        yes_no_input = input("Would you like to quit? (y/n): ")
        if yes_no_input.lower() == "y":
            print("You quitted the program. See you!")
        else:
            return display_main_menu()
    else:
        print("Choose a proper number! ")
        return display_main_menu()

def display_main_menu():
    """This function is used to show a main manu to a user"""
    text = """
    
    1. House owners.
    2. House renters.
    3. Exit. """

    print(text)

    user_input = int(input("Choose a number from menu: "))

    if user_input == 1:
        display_owner_register_menu()
    elif user_input == 2:
        display_renter_register_menu()
    elif user_input == 3:
        yes_no_input = input("Would you like to quit? (y/n): ")
        if yes_no_input.lower() == "y":
            print("You quitted the program. See you!")
        else:
            return display_main_menu()
    else:
        print("Choose a proper number! ")
        return display_main_menu()
    
if __name__ == "__main__":
    display_main_menu()