# Haqiqiy tipli, 16 ta elementdan iborat list yarating. 
# Minimal va maksimal elementlarini indeksi(joylashgan o`rinini) toping.

import random

def max_min_index(numbers_list):
    
    #genearting a list of random float numbers
    for i in range(16):
        numbers_list.append(random.random())
    
    #finding the index of maximum and minimum items of the list
    index_max_item = numbers_list.index(max(numbers_list))
    index_min_item = numbers_list.index(min(numbers_list))
    
    return f"The index of the the maximum item: {index_max_item},\nthe index of the minimum item: {index_min_item}"

user_list = []
print(max_min_index(user_list))
