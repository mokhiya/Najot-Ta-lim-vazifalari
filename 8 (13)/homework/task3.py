# Butun tipli, 10 ta elementdan iborat list yarating. 
# Maksimal elementini birinchi elementi bilan joyini almashtiring.

import random

numbers_list = []

for _ in range(10):
    numbers_list.append(random.randint(-100, 100)) #generating 12 random numbers and adding to the list 

numbers_list[0] = max(numbers_list) #changing the first element of the list with a maximum value
print(numbers_list)
