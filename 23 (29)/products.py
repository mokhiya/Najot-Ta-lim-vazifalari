import json 
import os

class JsonManager:
    """
    This class is applied to manage working with json files
    """
    file_name = 'products.json'


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



class Products(JsonManager):
    """
    This class represents info about products with basic attributes.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__total_summa = 0

    def get_total_price(self): 
        """
        This method calculates the total price of all products.
        """
        products = self.read_file()
        for product in products:
            self.__total_summa+= product["Price"]
        return f"A total sum of all products: {self.__total_summa}"


class Book(Products):
    """
    This class represents info about books with basic attributes.

    Attributes:
        name (str): The name of the book.
        price (int): The price of the book.
        type (str): A type of the product.
        pages (int): Total pages of the book.
    """
    
    def __init__(self, name, price, pages):
        super().__init__(name, price)
        self.type = "Book"
        self.pages = pages
        self.__total_summa = 0

    def change_to_dict(self):
        """
        This method is used to format a given data into dictionary
        """
        return {
            "Name": self.name,
            "Price": self.price,
            "Type":  self.type,
            "Pages": self.pages 
        }


    def show_all_data(self):
        """
        This method is used to show a stored data
        """
        products = self.read_file()
        data_str = ""
        for product in products:
            if product["Type"] == self.type:
                for key, value in product.items():
                    data_str += f"{key}: {value}\n"
        return f"Data:\n{data_str}"


    def get_total_price(self):
        """
        This method calculates the total price of all book products.
        """
        products = self.read_file()
        for product in products:
            if product["Type"] == self.type:
                self.__total_summa+= product["Price"]
        return f"A total sum of all books: {self.__total_summa}"


class Clothing(Products):
    """
    This class represents info about cloths with basic attributes.

    Attributes:
        name (str): The name of the cloth.
        price (int): The price of the cloth.
        type (str): A type of the product.
        color (str): Color of the cloth.
    """
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.type = "Clothing"
        self.color = color
        self.__total_summa = 0


    def change_to_dict(self):
        """
        This method is used to format a given data into dictionary
        """
        return {
            "Name": self.name,
            "Price": self.price,
            "Type":  self.type,
            "Color": self.color 
        }


    def show_all_data(self):
        """
        This method is used to show a stored data
        """
        products = self.read_file()
        data_str = ""
        for product in products:
            if product["Type"] == self.type:
                for key, value in product.items():
                    data_str += f"{key}: {value}\n"
        return f"Data:\n{data_str}"


    def get_total_price(self):
        """
        This method calculates the total price of all cloths.
        """
        products = self.read_file()
        for product in products:
            if product["Type"] == self.type:
                self.__total_summa+= product["Price"]
        return f"A total sum of all books: {self.__total_summa}"


class Electronics(Products):
    """
    This class represents info about electronics with basic attributes.

    Attributes:
        name (str): The name of the electronics.
        price (int): The price of the electronics.
        type (str): A type of the product.
        made_in (str): Where a product is made.
        year (int): Made year of the electronics.
    """
    def __init__(self, name, price, made_in, year):
        super().__init__(name, price)
        self.type = "Electronics"
        self.made_in = made_in
        self.year = year
        self.__total_summa = 0


    def change_to_dict(self):
        """
        This method is used to format a given data into dictionary
        """
        return {
            "Name": self.name,
            "Price": self.price,
            "Type":  self.type,
            "Made_in": self.made_in,
            "Year": self.year
        }


    def show_all_data(self):
        """
        This method is used to show a stored data
        """
        products = self.read_file()
        data_str = ""
        for product in products:
            if product["Type"] == self.type:
                for key, value in product.items():
                    data_str += f"{key}: {value}\n"
        return f"Data:\n{data_str}"
        

    def get_total_price(self):
        """
        This method calculates the total price of all electronic products.
        """
        products = self.read_file()
        for product in products:
            if product["Type"] == self.type:
                self.__total_summa+= product["Price"]
        return f"A total sum of all electronics: {self.__total_summa}"


book1 = Book(name="Alchemic", price=30000, pages=250)
#book1.add_onedata_to_file(book1.change_to_dict())
print(book1.get_total_price())
print(book1.show_all_data())
cloths = Clothing(name="T-shirt", price=25000, color="blue")
#cloths.add_onedata_to_file(cloths.change_to_dict())
print(cloths.get_total_price())
print(cloths.show_all_data())
electronic = Electronics(name="Phone", price= 1200000, made_in="China", year= 2021)
#electronic.add_onedata_to_file(electronic.change_to_dict())
print(electronic.get_total_price())
print(electronic.show_all_data())