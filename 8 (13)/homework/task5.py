#20 ta elementdan iborat butun tipli list yarating.
# Eng katta juft va eng katta toq sonlarni toping. 

import random

numbers_list = []

for _ in range(20):
    numbers_list.append(random.randint(-100, 100)) #generating 20 random numbers and adding to the list

for number in numbers_list:
    if number % 2 == 0: #if an item of the list is even
        max_value = max(numbers_list) #finding a maximum in the list 
    else:
        min_value = min(numbers_list) #else, finding a minimum value in the list

print(f"""Original list: {numbers_list},
a maximum item of the list: {max_value}, 
a minimum item of the list: {min_value}""")