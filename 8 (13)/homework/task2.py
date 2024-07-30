#Elementlari 12 ta butun son bo`lgan list yarating. 
#5-elementini shu list elementlarini o`rta arifmetigi qiymatiga almashtirib 
#yangi list hosil qiling. 

import random

numbers_list = []
summa = 0

for _ in range(12):
    numbers_list.append(random.randint(-99, 99)) #generating 12 random numbers and adding to the list 

for number in numbers_list: 
    summa += number #calculating the sum of each item

avarage_arithmetic = summa/12 #calculating an avarage aritmetic f the list items
print(f"Avarage arithmetic of the list is: {avarage_arithmetic}")

numbers_list[4] = avarage_arithmetic #changing fifth item with a result of the avar. arithmetic

print(numbers_list)
