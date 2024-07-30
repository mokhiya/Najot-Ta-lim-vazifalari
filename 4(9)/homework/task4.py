students_height = input("Enter your students' height with space (cm): ")

#Converting the string of heights into a list of floats
list_height = [float(height) for height in students_height.split()]

#Calculating the average height
avarage_height = sum(list_height)/len(list_height)

print(f"Avargae height in your group is: {avarage_height}")

#EXPLANATION to some of my codes:

#list comprehension. It is used to fasten the readibility of the code and to save a memory.
#in my case, we:
#1) splitted students height with spaces and saved as a list
#2) we looped each value of that list
#3) we casted each looped value to float
#4) we created a list called list_height and saved casted value