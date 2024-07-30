# Butun tipli, 9 ta elementdan iborat list yarating. 
# Maksimal elementini minimal elementi bilan joyini almashtiring.

import random

original_list = []

for _ in range(9):
    original_list.append(random.randint(-100, 100)) #generating 12 random numbers and adding to the list 
    copy_list = original_list.copy() #making a copy of the original list to compare the result

#finding indexes of min and max values of the list
max_index = original_list.index(max(original_list))
minimum_index = original_list.index(min(original_list))

#replacing min and max values
original_list[minimum_index], original_list[max_index] = original_list[max_index], original_list[minimum_index]

print(f"Original list: {copy_list}\nChanged list: {original_list}")