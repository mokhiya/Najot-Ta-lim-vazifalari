"""Mashinalarni ijaraga berish va olishni boshqarish uchun class yozish kerak: 
Attributes: name, model, (is_rented=False ushbu attribute ni odam kiritmaysi siz uni o'zingiz yaratib qo'yasiz 
va False ga tenglab qo'yasiz.) 
Methods: 
1. add_car(name, model) 
2. rent(name) -> agar shu mashina is_rented false bo'lsa uni True ga o'girish kerak va mashina haqida malumotni odamga berish kerak 
4. return_car(name) -> mashina ro'yxatda bor bo'lsa is_rented ni false ga o'girish kerak
"""

import csv
import os

class CarRenting:
    """
    A class representing a car rental system.
    """

    def __init__(self, name, model):
        """
        This method is used to initialize a new instance of the CarRenting class.

        Args:
            name (str): The name of the car.
            model (str): The model of the car.
        """
        self.name = name
        self.model = model
        self.is_rented = False

    @staticmethod
    def add_car(name, model):
        """
        This method is used to add a car to the list file.

        Args:
            name (str): The name of the car.
            model (str): The model of the car.
        Returns:
            str
        """
        car_data = [name, model, "False"]
        file_exists = os.path.exists("cars.csv")
        with open("cars.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Name", "Model", "Is_Rented"])  # Write the header row
            writer.writerow(car_data)
        return f"Car {name} ({model}) has been added to the list."


    @staticmethod
    def update_car_status(name, model, is_rented):
        """
        This method is used to update the rental status of a car.

        Arguments:
            name (str): The name of the car.
            model (str): The model of the car.
            is_rented (bool): The new rental status of the car.
        Returns:
            str
        """
        if not os.path.exists("cars.csv"):
            return "No cars available in the list."
        car_data = []
        with open("cars.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name and row[1] == model:
                    row[2] = str(is_rented)
                car_data.append(row)

        with open("cars.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(car_data)
        return f"Car {name} ({model}) status has been updated."


    def rent_car(self):
        """
        This method is used to rent the car.
        Returns:
            str
        """
        if not self.is_rented:
            self.is_rented = True
            CarRenting.update_car_status(self.name, self.model, True)
            return f"Car {self.name} ({self.model}) is now rented."
        else:
            return f"Car {self.name} ({self.model}) is already rented."


    def return_car(self):
        """
        The method is used to return the rented car.
        Returns:
            str.
        """
        if self.is_rented:
            self.is_rented = False
            CarRenting.update_car_status(self.name, self.model, False)
            return f"Car {self.name} ({self.model}) has been returned."
        else:
            return f"Car {self.name} ({self.model}) was not rented."



car1 = CarRenting("Toyota", "Camry")
car1.add_car("Toyota", "Camry")
print(car1.rent_car())
print(car1.return_car())