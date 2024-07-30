from abc import ABC, abstractmethod 

# class Student(ABC):
    
#     @abstractmethod
#     def name(self):
#         raise NotImplementedError("Not implemented")

# class Person(Student):
#     def name(self):
#         return "Mohi"

# person = Person()
# print(person.name())

"""
Course base class, register, cancel_register, show_users

Math -> name, price, teacher, time
Dance -> name, price, teacher, time, age
Music -> name, price, teacher, type
"""
import json
import os
from abc import ABC, abstractmethod
from typing import Union


class JsonManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def check_existence(self):
        return os.path.exists(self.file_name)

    def read(self):
        if self.check_existence():
            if os.path.getsize(self.file_name) != 0:
                with open(self.file_name, 'r') as file:
                    data = json.load(file)
                    return data
            return []
        return []

    
    def write(self, all_data):
        with open(self.file_name, mode='w') as file:
            json.dump(all_data, file, indent=4)
            return "Data is added"

    def add(self, data: dict):
        all_data = self.read()
        all_data.append(data)
        return self.write(all_data)


class Course(ABC, JsonManager):
    def __init__(self, name, price, teacher):
        super().__init__(file_name="courses.json")
        self.name = name
        self.price = price
        self.teacher = teacher

    def parent_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "teacher": self.teacher,
            "users": []
        }

    @abstractmethod
    def register(self):
        raise NotImplementedError("You must implement register method")

    @abstractmethod
    def cancel_register(self):
        raise NotImplementedError("You must implement cancel_register")

    @abstractmethod
    def show_users(self):
        raise NotImplementedError("You must implement show_users")


class Math(Course):
    def __init__(self, name, price, teacher, time):
        super().__init__(name, price, teacher)
        self.file_name = "math.json"
        self.time = time

    def dict(self):
        data = self.parent_dict()
        data["time"] = self.time
        return data

    def add_to_file(self):
        return self.add(self.dict())

    def register(self):
        pass

    def cancel_register(self):
        pass

    def show_users(self):
        return self.read()


class Dance(Course):
    def __init__(self, name, price, teacher, age):
        super().__init__(name, price, teacher)
        self.age = age
        self.file_name = "dance.json"

    def dict(self):
        data = self.parent_dict()
        data["age"] = self.age
        return data

    def add_to_file(self):
        return self.add(self.dict())

    def register(self):
        pass

    def cancel_register(self):
        pass

    def show_users(self):
        return self.read()


class Music(Course):
    def __init__(self, name, price, teacher, type_of_music):
        super().__init__(name, price, teacher)
        self.type_of_music = type_of_music
        self.file_name = "music.json"

    def dict(self):
        data = self.parent_dict()
        data["type_of_music"] = self.type_of_music
        return data

    def add_to_file(self):
        return self.add(self.dict())

    def register(self):
        pass

    def cancel_register(self):
        pass

    def show_users(self):
        return self.read()


# 
# def register_user(type_of_course):
#     if type_of_course == "math":
#         assert async async async 
#     elfi 
    

math1 = Math(name="Math 01", price=10000, teacher="Sanjarbek", time="10:00")
math1.add_to_file()

