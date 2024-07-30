""" Tomoshabinlar konsertga bilet sotib olishlari uchun quyidagicha dastur yozing: 
Class Concert: author, date, total_tickets, price 
Methods: 
get_price() 
get_full_info() 
buy_ticket(full_name, phone_number, quantity) 
save_to_file() 
available_tickets_count() 
sold_tickets_count() 
read_data() 
User bilar olgandan keyin total_tickers kamayib borishi kerak, 
agar bilet tugasa sotib ola olmaydi """

import csv
import os

class Concert:
    def __init__(self, author, date, total_tickets, price):
        """
        Ticket price.
            tickets_sold (int): Number of tickets sold.
        """
        self.author = author
        self.date = date
        self.total_tickets = total_tickets
        self.price = price
        self.tickets_sold = 0

    def get_price(self):
        """
        Getting the ticket price.
        Returns:
            float: Ticket price.
        """
        return self.price

    def get_full_info(self):
        """
        Getting full concert information.
        Returns:
            str: Formatted concert details.
        """
        return f"Concert by {self.author} on {self.date}. Tickets available: {self.available_tickets_count()}"

    def buy_ticket(self, full_name, phone_number, quantity=1):
        """
        Buying concert tickets.

        Args:
            full_name (str): Full name of the ticket buyer.
            phone_number (int): Phone number of the ticket buyer.
            quantity (int): Number of tickets to purchase (default is 1).
        Returns:
            str: Purchase confirmation or sold-out message.
        """
        if self.available_tickets_count() >= quantity:
            self.tickets_sold += quantity
            return f"Thank you, {full_name}! You've purchased {quantity} ticket(s). Your phone number is {phone_number}."
        else:
            return "Sorry, tickets are sold out."

    def save_to_file(self, full_name, phone_number, quantity=1):
        """
        Saving ticket purchase data to a CSV file.
        Args:
            full_name (str): Full name of the ticket buyer.
            phone_number (int): Phone number of the ticket buyer.
            quantity (int): Number of tickets purchased (default is 1).
        """
        filename = "data.csv"
        if not os.path.exists(filename):
            with open(file=filename, mode="w", newline='', encoding="UTF-8") as file:
                writer = csv.writer(file)
                writer.writerow(["full name", "phone number", "quantity"])
        else:
            with open(file=filename, mode="a", newline='', encoding="UTF-8") as file:
                writer = csv.writer(file)
                writer.writerow([full_name, phone_number, quantity])


    def available_tickets_count(self):
        """
        Calculating the number of available tickets.
        Returns:
            int: Number of available tickets.
        """
        return self.total_tickets - self.tickets_sold

    def sold_tickets_count(self):
        """
        Getting the total number of tickets sold.
        Returns:
            int: Number of tickets sold.
        """
        return self.tickets_sold

    def read_data(self):
        """
        Reading ticket purchase data from the CSV file.
        Prints:
            str: Formatted ticket purchase information.
        """
        if os.path.exists("data.csv"):
            with open(file="data.csv", mode="r", newline='', encoding="UTF-8") as file:
                reader = csv.reader(file)
                next(reader)  # Skipping the header row
                for row in reader:
                    full_name, phone_number, quantity = row
                    print(f"Full Name: {full_name}, Phone Number: {phone_number}, Quantity: {quantity}")
        else:
            print("File does not exist")



data = Concert("Alisher Fayz", "18-12-2024", 150, 50000)
print(data.author)  
print(data.available_tickets_count())
print(data.buy_ticket("Mohi", 998946718299, 2)) 
print(data.get_full_info())
data.save_to_file("Mohi", 998946718299, 2)
data.read_data()


