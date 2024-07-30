"""
Create a base class FileHandler with a method read(). Implement subclasses
    TextFileHandler, CSVFileHandler, and JSONFileHandler, each overriding the read()
    method to handle different file types. Write a function that takes a list of
    FileHandler objects and calls their read() methods.
"""

class FileHandler:
    def read_file(self):
        return "File is read"

class TextFileHandler(FileHandler):
    def read_file(self):
        return "Text file is read"

class CSVFileHandler(FileHandler):
    def read_file(self):
        return "CSV file is read"

class JSONFileHandler(FileHandler):
    def read_file(self):
        return "Json file is read"

file1= FileHandler()
print(file1.read_file())


# import os, json, csv

# class DataFormatter:
#     def format(self, data: dict, filename):
#         with open(file=filename, mode= 'w') as file:
#             file.write(data)

# class JSONFormaater(DataFormatter):
#     def format(self, data: dict, filename):
#         if not os.path.exists(filename):
#             with open(file=filename, mode="w") as json_file:
#                 json.dump(data, json_file, indent= 4)
#         else:
#             with open(file=filename, mode="a") as json_file:
#                 json.dump(data, json_file, indent= 4)


# class TextFormatter:
#     def format(self, data: dict, filename):
#         if not os.path.exists(filename):
#             with open(file=filename, mode="w") as txt_file:
#                 txt_file.write(data)

#         else:
#             with open(file=filename, mode="a") as txt_file:
#                 txt_file.write(data)

# class CSVFormatter:
#     def format(self, data: dict, filename):
#         if not os.path.exists(filename):
#             with open(file=filename, mode="w", newline="") as csv_file:
#                 data_writer = csv.writer(data)
#         else:
#             with open(file=filename, mode="a", newline="") as csv_file:
#                 data_writer = csv.writer(data)

import json 
import os

class JsonManager:
    file_name = 'products.json'

    def check_existance(self):
        return os.path.exists(self.file_name)

    def read_file(self):
        if self.check_existance():
            if os.path.getsize(self.file_name) != 0:
                with open(self.file_name, mode="r") as file:
                    data =  json.load(file)
                    return data
            return []
        return []
        

    def write_file(self, all_data):
        with open(self.file_name, mode= "w") as file:
            json.dump(all_data, file, indent=4)
            return "Data is written to a file"

    def add_onedata_to_file(self, data: dict):
        all_data = self.read_file()
        all_data.append(data)
        return self.write_file(all_data)

class Products(JsonManager):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__total_summa = 0

    def get_total_price(self): 
        products = self.read_file()
        for product in products:
            self.__total_summa+= product["Price"]
        return f"A total sum of all products: {self.__total_summa}"

class Book(Products):
    def __init__(self, name, price, pages):
        super().__init__(name, price)
        self.type = "Book"
        self.pages = pages
        self.__total_summa = 0

    def change_to_dict(self):
        return {
            "Name": self.name,
            "Price": self.price,
            "Type":  self.type,
            "Pages": self.pages 
        }


    def show_all_data(self):
        products = self.read_file()
        data_str = ""
        for product in products:
            if product["Type"] == self.type:
                for key, value in product.items():
                    data_str += f"{key}: {value}\n"
        return f"Data:\n{data_str}"

    def get_total_price(self):
        products = self.read_file()
        for product in products:
            if product["Type"] == self.type:
                self.__total_summa+= product["Price"]
        return f"A total sum of all books: {self.__total_summa}"


class Clothing(Products):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.type = "Clothing"
        self.color = color
        self.__total_summa = 0

    def change_to_dict(self):
        return {
            "Name": self.name,
            "Price": self.price,
            "Type":  self.type,
            "Color": self.color 
        }

    def show_all_data(self):
        products = self.read_file()
        data_str = ""
        for product in products:
            if product["Type"] == self.type:
                for key, value in product.items():
                    data_str += f"{key}: {value}\n"
        return f"Data:\n{data_str}"

    def get_total_price(self):
        products = self.read_file()
        for product in products:
            if product["Type"] == self.type:
                self.__total_summa+= product["Price"]
        return f"A total sum of all books: {self.__total_summa}"


class Electronics(Products):
    def __init__(self, name, price, made_in, year):
        super().__init__(name, price)
        self.type = "Electronics"
        self.made_in = made_in
        self.year = year
        self.__total_summa = 0

    def change_to_dict(self):
        return {
            "Name": self.name,
            "Price": self.price,
            "Type":  self.type,
            "Made_in": self.made_in,
            "Year": self.year
        }

    def show_all_data(self):
        products = self.read_file()
        data_str = ""
        for product in products:
            if product["Type"] == self.type:
                for key, value in product.items():
                    data_str += f"{key}: {value}\n"
        return f"Data:\n{data_str}"
        

    def get_total_price(self):
        products = self.read_file()
        for product in products:
            if product["Type"] == self.type:
                self.__total_summa+= product["Price"]
        return f"A total sum of all electronics: {self.__total_summa}"


book1 = Book(name="Alchemic", price=30000, pages=250)
#book1.add_onedata_to_file(book1.change_to_dict())
print(book1.get_total_price())
cloths = Clothing(name="T-shirt", price=25000, color="blue")
#cloths.add_onedata_to_file(cloths.change_to_dict())
print(cloths.get_total_price())
electronic = Electronics(name="Phone", price= 1200000, made_in="China", year= 2021)
electronic.add_onedata_to_file(electronic.change_to_dict())
print(electronic.get_total_price())
print(electronic.show_all_data())