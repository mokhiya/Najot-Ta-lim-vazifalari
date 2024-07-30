# import datetime

# def expiring_card_date ():
#     current_date = str(datetime.date.today()).split("-")
#     expire_year = str(int(current_date[0]) + 5)
#     expire_date = f"{current_date[1]}/{expire_year[2:]}"
#     return expire_date

# print(expiring_card_date())
import random
card_number = str(random.randint(10**15, 9999999999999999))
for i in range(0, len(card_number), 4)): 
    formatted_card_number = ' '.join(card_number[i:i+4] 
print(card_number[i:i+4])