summa = 0

for number in range(1, 100): 
    if number % 4 == 0: #Checking if the number is divisible by 4
        summa += number #If true, we are add the number to a variable called summa

print(summa)