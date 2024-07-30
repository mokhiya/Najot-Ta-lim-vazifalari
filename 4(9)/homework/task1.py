multiplication = 1

for number in range(-80, 80): #looping each number in the range from -80 to 80
    
    if number % 7 == 0 and number % 2 != 0: #checking if the number is divisible by 7 and if the number is odd
        
        multiplication *= number #if true, multiplying those numbers to each other

print(multiplication)

