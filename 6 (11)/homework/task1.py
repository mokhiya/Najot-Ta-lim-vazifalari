# 1 dan 100 gacha bo'lsa 
#sonlar uchun raqamlar yig'indisi 5 ga karrali bo'lgan sonlar sonini toping. 
Numbers = []

for number in range(1, 100):
    
    if len(str(number)) == 2: #checking if the number is 2-digit
        digit_1 = number // 10 #getting the fisrt digit
        digit_2 = number % 10  #getting the second digit
        
        if (digit_1 + digit_2) % 5 == 0:  #if a summa of two digits is dividible by 5
            Numbers.append(number)   #adding the number to an empty list

print(f"Numbers divisible by 5 are: {Numbers}")
