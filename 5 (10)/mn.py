number_m = int(input("enter m number: "))
number_n = int(input("enter n number: "))
text = ""
for i in range(1, number_n):
    
    if i**2 > number_m:
        text += str(i)
print(text[0])