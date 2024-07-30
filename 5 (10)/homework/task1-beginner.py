number = input("Enter a natural number: ")

number_list = list(number)
count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
count_8 = 0
count_9 = 0
   
for i in range(len(number)):
    if number_list[i] == "0":
        count_0 += 1
    elif number_list[i] == "1":
        count_1 += 1
    elif number_list[i] == "2":
        count_2 += 1
    elif number_list[i] == "3":
        count_3 += 1
    elif number_list[i] == "4":
        count_4 += 1
    elif number_list[i] == "5":
        count_5 += 1
    elif number_list[i] == "6":
        count_6 += 1
    elif number_list[i] == "7":
        count_7 += 1
    elif number_list[i] == "8":
        count_8 += 1
    elif number_list[i] == "9":
        count_9 += 1
print(f"""digit 0: {count_0} \tdigit 1: {count_1} 
\ndigit 2: {count_2} \tdigit 3: {count_3} 
\ndigit 4: {count_4} \tdigit 5: {count_5} 
\ndigit 6: {count_6} \tdigit 7: {count_7} 
\ndigit 8: {count_8} \tdigit 9: {count_9}""")