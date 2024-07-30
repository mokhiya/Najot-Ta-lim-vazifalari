# Haqiqiy tipli, 14 ta elementdan iborat list yarating. 
# 1 dan 7 gacha bo`lgan elementlarini ko`payish, 
# 8 dan 14 gacha bo`lgan elementlarini kamayish tartibida joylashtiring.

import random

def ascending_descending_numbers(numbers_list):

    sorted_list = []
    #generating 14 random float numbers in the list that are in range from 1 to 100
    for _ in range(14):
        numbers_list.append(random.uniform(1, 100))
    
    #slicing first 7 and next 7 items of the list for next purposes
    first_half = numbers_list[0:7]
    second_half = numbers_list[7:]

    #sorting first- and second-half items, and adding them to a list
    sorted_first_half = sorted(first_half)
    sorted_list.append(sorted_first_half)
    sorted_second_half = sorted(second_half, reverse = True)
    sorted_list.append(sorted_second_half)
    
    return sorted_list

users_list = []
print(ascending_descending_numbers(users_list))
