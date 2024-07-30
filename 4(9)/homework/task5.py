number = int(input("Enter a number: "))

for num in range(2, number + 1):
    for i in range(2, num): #Checking if the number is divisible by any number other than 1 and itself
         if (num % i) == 0: #If the number is divisible by another number, it's not prime
             break
    
    else: #otherwise, it is a prime number, we print it
        print(num)