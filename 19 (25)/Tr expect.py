
import os
import json

def adding_product():
    product_name = input("Enter a product: ").strip().title()
    price = float(input("Enter price: "))

    products = {
        'Product': product_name,
        'Price': price
    }

    return products

def asking_user():

    user_product = input("Enter a product: ")
    quantity = int(input("How many do you want? "))

    if user_product in adding_product(products):
        pass



file_path = "data.csv"

def adding_product():
    product_name = input("Enter a product: ").strip().title()
    price = float(input("Enter price: "))

    data = [product_name, price]

def writing_product_data(product_name, price):
    

    if not os.excists(file_path):
        with open(file=file_path, mode="w", encoding="UTF-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Product name", "Price", "Summa"])
    
    product_data = product_name, price









prodcts = {

}