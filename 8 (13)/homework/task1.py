#Elementlari 14 ta butun son bo`lgan list yarating. 
# Qiymati juft bo`lgan elementlari sonini toping. 

import random

numbers_list = []
even_numbers_counter = 0

for _ in range(14):
    numbers_list.append(random.randint(1, 100)) #generating 14 random numbers and adding to the list 
    
for num in numbers_list: #iterating each element of the list
    
    if num % 2 == 0: #cheking if the element is even
        even_numbers_counter += 1  #if yes, counting their quantity

print(f"Even numbers in total: {even_numbers_counter}")