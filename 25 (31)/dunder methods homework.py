""" Student nomli class yarating va 
unda quyidagi amallarni bajara olishim uchun dunder methodlar yozing 
undan quyidagicha attributelar bo'lishi kerak: 
full_name, age, birthday, gender, courses=[] 
biror bir objectni chaqarib unga yangi object ni berib yuborsam 
o'zini ichidagi courses listiga shu objectni qo'shib qo'ysin 
+, -, *, /, +=, -=, /=, *=, ** 
object ni uzunligini o'lchasam jami courselarni sonini chiqarib bersin 
hech qanday menyu yasash kerak emas shunchaki har bir methodni tekshirib ko'rish kerak """

class Student:
    """
    This class represents a student with personal information and enrolled courses.

    Attributes:
        full_name (str): The full name of the student.
        age (int): The age of the student.
        birthday (str): The birthday of the student (e.g., "June 8").
        gender (str): The gender of the student.
        courses (list): A list of courses the student is enrolled in.

    Methods:
        __call__(*args, **kwargs): Adds courses to the student's course list.
        __repr__(): Returns a string representation of the student.
        __add__(other): Adds the ages of two students.
        __sub__(other): Subtracts the ages of two students.
        __mul__(factor): Multiplies the student's age by a numeric factor.
        __truediv__(divisor): Divides the student's age by a non-zero divisor.
        __iadd__(name): Adds a name to the student's full name.
        __isub__(name): Removes a name from the student's full name.
        __imul__(factor): Multiplies the student's age by a numeric factor (in-place).
        __itruediv__(divisor): Divides the student's age by a non-zero divisor (in-place).
        __pow__(exponent): Raises the student's age to a given exponent.
        __len__(): Returns the number of courses the student is enrolled in.
    """
    def __init__(self, full_name, age, birthday, gender):
        self.full_name = full_name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.courses = []

    def __call__(self, *args, **kwargs):
        for course in args:
            if isinstance(course, str):
                self.courses.append(course)

    def __repr__(self):
        return f"{self.full_name} is {self.age} years old"

    def __add__(self, other):
        if isinstance(other, Student):
            result = self.age + other.age
            return f"Students are {result} years old"
        else:
            raise TypeError("Can only add two Student objects")

    def __sub__(self, other):
        if isinstance(other, Student):
            result = self.age - other.age
            return f"Students are {result} years old"
        else:
            raise TypeError("Can only subtract two Student objects")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Student(full_name=f"{self.full_name} (multiplied)", age=self.age * factor, birthday=self.birthday, gender=self.gender)
        else:
            raise TypeError("Can only multiply by a numeric value")

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)) and divisor != 0:
            return Student(full_name=f"{self.full_name} (divided)", age=self.age / divisor, birthday=self.birthday, gender=self.gender)
        else:
            raise ValueError("Invalid divisor for division")

    def __iadd__(self, name):
        if isinstance(name, str):
            self.full_name += f" {name}"
            return self
        else:
            raise TypeError("Can only add a name (string)")

    def __isub__(self, name):
        if isinstance(name, str):
            self.full_name = self.full_name.replace(name, "")
            return self
        else:
            raise TypeError("Can only remove a name (string)")

    def __imul__(self, factor):
        if isinstance(factor, (int, float)):
            self.age *= factor
            return self
        else:
            raise TypeError("Can only multiply age by a numeric value")

    def __itruediv__(self, divisor):
        if isinstance(divisor, (int, float)) and divisor != 0:
            self.age /= divisor
            return self
        else:
            raise ValueError("Invalid divisor for division")

    def __pow__(self, exponent):
        if isinstance(exponent, int):
            return Student(full_name=f"{self.full_name} (to the power of {exponent})", age=self.age ** exponent, birthday=self.birthday, gender=self.gender)
        else:
            raise TypeError("Exponent must be an integer")
    
    def __len__(self):
        return len(self.courses)

# Example usage:
student1 = Student(full_name="Anora Malikova", age=18, birthday="June 8", gender="female")
student2 = Student(full_name="Akamal Saidov", age=20, birthday="June 15", gender="male")
student1("Maths", "Music")
student2("English")
print(student1.courses, student2.courses) # Adding courses to the course list
print(student1) # For str method
print(student1 + student2)  # Adding ages
print(student1 - student2)  # Subtracting ages
print(student1 * 1.5)       # Multipling age
print(student2 / 2)         # Dividing age
student1 += "Solijonova"         # Adding a name
student2 -= "Saidov"        # Removing a name
print(student1.full_name, student2.full_name)
print(student1 ** 2)        # Age to the power of 2
print(len(student1.courses)) # Measuring the length of courses



