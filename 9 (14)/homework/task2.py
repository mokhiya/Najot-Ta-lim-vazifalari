# Butun tipli, 14 ta elementdan iborat list yarating 
# uni ichida ham musbat ham manfiy bo'lsin. 
# Musbat sonlarning toqlari yig`indisini va sonini xisoblang.

import random

def summa_odd_numbers(numbers_list):

    summa = 0
    counter = 0

    #generating 14 random integer numbers in the list
    for _ in range(14):
        numbers_list.append(random.randint(-99, 99))

    for numbers in numbers_list:
        
        #checking if the number is postive and odd
        if numbers > 0 and numbers % 2 != 0:
            
            #if yes, calculating the sum and the number of positive-odd numbers
            summa += numbers
            counter += 1

    return f"The sum of odd numbers: {summa}, the number of odd numbers: {counter}"

users_list = []
print(summa_odd_numbers(users_list))



