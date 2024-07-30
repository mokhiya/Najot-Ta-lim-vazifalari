#  Odamdan 2 ta son so'rang va raqamlari yig'indisi kattasini qaytaring. 
#  Masalan: 91 va 67 bo'lsa 9 + 1 = 10 va 6 + 7 = 13 demak 67 ni qaytarasiz.

Number1 = int(input("Enter the first number: "))
Number2 = int(input("Enter the second number: "))

#casting Number1 and Number2 to string to iterate each digit, then casting them to integer again
#and calculating the sum of each digit
sum1 = sum(int(digit) for digit in str(Number1)) 
sum2 = sum(int(digit) for digit in str(Number2))

if sum1 > sum2:
    print(f"{Number1} is larger than {Number2}")
elif sum1 < sum2:
    print(f"{Number2} is larger than {Number1}")
else:
    print(f"{Number1} and {Number2} are equal")

