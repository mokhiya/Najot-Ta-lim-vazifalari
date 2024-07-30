import os
import json


class JsonManager:
    def __init__(self, file_name):
        self.file_name = file_name


    def _file_exists_and_not_empty(self):
        return os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0


    def read(self):
        if self._file_exists_and_not_empty():
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []


    def write(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)


    def add_data(self, data: dict):
        all_data = self.read()
        all_data.append(data)
        self.write(all_data)
        return "Data added successfully"


    def update_data(self, index: int, data: dict):
        all_data = self.read()
        all_data[index] = data
        self.write(all_data)
        return "Data updated successfully"


    def delete_data(self, index: int):
        all_data = self.read()
        all_data.pop(index)
        self.write(all_data)
        return "Data deleted successfully"


    def find_user_index_by_email(self, email):
        all_users = self.read()
        for index, user in enumerate(all_users):
            if user['email'] == email:
                return index
        return None


    def find_house_by_city(self, city):
        all_houses = self.read()
        for house in all_houses:
            if house['city'] == city:
                return house
        return None

renter_manager = JsonManager(file_name= "renters.json")
owner_manager = JsonManager(file_name= "owners.json")