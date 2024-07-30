print("Palindromic numbers: \n")

for number in range(100):
    if str(number) == str(number)[::-1]: #checking if the number is equal to its reverse version
        
        print(number)