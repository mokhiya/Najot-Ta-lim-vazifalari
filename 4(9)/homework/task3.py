count = 0
count_2 = 0

for tickets in range(1000000):
    
    #Converting the ticket number to a string, because python will automatically remove leading zeros 
    #and padding with zeros if a looped digit is less than 6
    ticket_str = str(tickets).zfill(6) 

    first_three_numbers = ticket_str[:3] #Getting the first three digits
    last_three_numbers = ticket_str[3:]  #Geting the last three digits

    if first_three_numbers == last_three_numbers:
        count += 1
        print(f"Lucky ticket: {ticket_str}")

        #now converting each three-digit string numbers to integer 
        #and calculating their sums
        first_three_numbers_sum = sum(int(digit) for digit in first_three_numbers)
        second_three_numbers_sum = sum(int(digit) for digit in last_three_numbers)

        #checking if one of those sums are equal to 13
        if first_three_numbers_sum == 13 or second_three_numbers_sum == 13:
            count_2 += 1
            print(f"tickets which a sum of first or second numbers is equal to 13: {ticket_str}")


print(f"A number of lucky tickets is: {count}")
print(f"A number of lucky tickets where the sum of the first or second three numbers is equal to 13: {count_2}")


#EXPLANATION to some of codes:
#1. zfill() method is used to fill strings with zeros up to a given witdh.
#if I write text = 25; text = text.zfill(3) it outputs: 025.

#2. Generator expression.
#it is used with () and helps to save a memory and speed readibility of a code.