# class Operations:
#     def __init__(self, number1, number2):
#         self.number1 = number1
#         self.number2 = number2
        
    
#     def adding_numbers(self):
    
#         addition_result = self.number1 + self.number2
#         return addition_result
    
#     def subtraction_numbers(self):
   
#         subtraction_result = self.number1 - self.number2
#         return subtraction_result

#     def dividing_numbers(self):
    
#         division_result = self.number1 / self.number2
#         return division_result
    
#     def multiplying_numbers(self):
    
#         multiplication_result = self.number1 * self.number2
#         return multiplication_result


# opreration = Operations(25, 24)
# print(opreration.adding_numbers())
# print(opreration.dividing_numbers())
# print(opreration.multiplying_numbers())
# print(opreration.subtraction_numbers())
import os, csv

class CsvManager:
    def __init__(self, filename):
        self.filename = filename


    def check_excistance(self):
        if os.path.exists(self.filename):
            return True
        return False

    def create_csv_file(self):
        if not self.check_excistance():
            with open(self.filename, mode= "x", newline ='', encoding= "UTF-8") as file:
                return "File has been created"
        return "File exists"
    

    def write_csv_file(self, name, age):
        with open(self.filename, mode= "w", newline='', encoding="UTF-8") as file:
            writer_file = csv.writer(file)
            writer_file.writerow([name, age])
        return "Data has been written"


    def read_csv_file(self):
        if self.check_excistance:
            with open(self.filename,  mode= "r", newline ='', encoding= "UTF-8") as file:
                reader_file = csv.reader(file)
                for row in reader_file:
                    return [row]
        return []

file1 = CsvManager("users.csv")
print(file1.check_excistance())
print(file1.create_csv_file())
print(file1.read_csv_file())
print(file1.write_csv_file("Mohi", 15))