import json 
import os
from abc import ABC, abstractmethod

class JsonManager:
    """
    This class is applied to manage working with json files
    """
    file_name = 'data.json'


    def check_existance(self):
        """
        This method checks the existance of the file
        """
        return os.path.exists(self.file_name)


    def read_file(self):
        """
        This method reads the data of the file
        """
        if self.check_existance():
            if os.path.getsize(self.file_name) != 0:  # if the file is not empty
                with open(self.file_name, mode="r") as file:
                    data = json.load(file)
                    return data
            return []
        return []
        

    def write_file(self, all_data):
        """
        This method writes all data into the file
        """
        with open(self.file_name, mode= "w") as file:
            json.dump(all_data, file, indent=4)
            return "Data is written to a file"


    def add_onedata_to_file(self, data: dict):
        """
        This method writes one given data into the the file
        """
        all_data = self.read_file()
        all_data.append(data)
        return self.write_file(all_data)
    
    def show_all_data(self):
        """
        This method is used to show a stored data
        """
        products = self.read_file()
        data_str = ""
        for product in products:
            for key, value in product.items():
                data_str += f"{key}: {value}\n"
        return f"All data:\n\n{data_str}"

class Shape(ABC, JsonManager):
    """
    This calss is abstract base class (ABC) inherited from JsonManager class
    
    Methods(abstract): 
        - get_area() 
        - get_perimeter()
    """
    @abstractmethod
    def get_area(self):
        return "This returns area of the shape"
    
    
    @abstractmethod
    def get_perimetr(self):
        return "This returns perimetr of the shape"


class Rectangle(Shape):
    """
    This class is applied to get various info about rectangle.

    Attributes:
        a (float): Length of one side of the rectangle.
        b (float): Length of the other side of the rectangle.
        S (float): Area of the rectangle (calculated using get_area()).
        P (float): Perimeter of the rectangle (calculated using get_perimeter()).
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.S = self.get_area()
        self.P = self.get_perimetr()


    def get_area(self):
        """
        This method calculates the area of circle
        """
        S = self.a * self.b 
        return f"The area of the rectangle is: {S}"


    def get_perimetr(self):
        """
        This method calculates the perimetr of rectangle
        """
        P = 2 * (self.a + self.b)
        return f"The perimetr of the rectagle is: {P}"


    def change_to_dict(self):
        """
        This method is used to format a given data into dictionary
        """
        return {
            "a": self.a,
            "b": self.b,
            "Perimetr": self.P,
            "Area": self.S 
        }

p = 3.14  # Global variable

class Circle(Shape):
    """
    This class is applied to get various info about circle.

    Attributes:
        r (float): Radius of the circle.
        S (float): Area of the cicrcle (calculated using get_area()).
        P (float): Perimeter of the circle (calculated using get_perimeter()).
    """
    
    def __init__(self, r):
        self.r = r
        self.S = self.get_area()
        self.P = self.get_perimetr()


    def get_area(self):
        """
        This method calculates the area of circle
        """
        p = 3.14
        S = p * (self.r ** 2)
        return f"The area of the circle is: {S}"


    def get_perimetr(self):
        """
        This method calculates the perimetr of circle
        """
        p = 3.14
        P = 2 * p * self.r
        return f"The perimeter of the circle is: {P}"


    def change_to_dict(self):
        """
        This method changes a given data into a dictionary format
        """
        return {
            "Radius": self.r,
            "Area": self.S,
            "Perimeter": self.P
        }


def display_menu():
    """
    This function displays the main menu and handle user input.
    """
    menu = """
    Options:
    1. Finding the area of the circle. 
    2. Finding the perimetr of the circle.
    3. Finding the area of the rectangle. 
    4. Finding the perimetr of the rectangle. 
    5. Displaying all results. 
    6. Exit. 
    """
    print(menu)

    user_input = int(input("Choose an option from the menu. Press a number: "))

    if user_input == 1:
        try:
            r = float(input("Enter the radius of the circle: "))
        except ValueError:
            print("Please, enter a number only.")
            r = float(input("Enter the radius of the circle: "))
        
        radius = Circle(r)
        print(radius.get_area())
        radius.add_onedata_to_file(radius.change_to_dict())
        display_menu()

    elif user_input == 2:
        try:
            r = float(input("Enter the radius of the circle: "))
        except ValueError:
            print("Please, enter a number only.")
            r = float(input("Enter the radius of the circle: "))

        radius = Circle(r=r)
        print(radius.get_perimetr())
        radius.add_onedata_to_file(radius.change_to_dict())
        display_menu()

    elif user_input == 3:
        try:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
        except ValueError:
            print("Please, enter a number only.")

        rectangle = Rectangle(a, b)
        print(rectangle.get_area())
        rectangle.add_onedata_to_file(rectangle.change_to_dict())
        display_menu()

    elif user_input == 4:
        rectangle = Rectangle(a, b)
        print(rectangle.get_perimetr())
        rectangle.add_onedata_to_file(rectangle.change_to_dict())
        display_menu()

    elif user_input == 5:
        data = JsonManager()
        print(data.show_all_data())
        display_menu()
    
    elif user_input == 6:
        yes_no_input = input("Would you like to quit? (y/n): ")
        if yes_no_input.lower() == "y":
            print("You quit the program. See you!")
        else:
            return display_menu()
    else:
        print("Choose a proper number! ")
        return display_menu()

# starting the program
display_menu()