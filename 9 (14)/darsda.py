# week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# while True: 
#     user_response = input("Please, enter a week day: ").title()
#     if user_response in week_days:
#         day = week_days.index(user_response)
#         print(day)
#         break
#     else:
#         print("No such a day in a week")
#         print(input("Please, enter a week day: ").title())


# def delete_repetition(numbers_list):

#     new_list = []
#     for num in numbers_list:
#         if numbers_list.count(num) == 1:
#             new_list.append(num)
            
#     return new_list

# users_list = [1, 22, 22, 5, 6]
# result = delete_repetition(users_list)
# print(result)

def change_repetition(numbers_list1, numbers_list2):

    for nums in numbers_list1:
        if nums in numbers_list2:
            index = numbers_list2.index(nums)
            numbers_list1[index] = 0
    
    return numbers_list1

users_list1 = [1, 2, 3, 4]
users_list2 = [1, 1, 2, 5]
result = change_repetition(users_list1, users_list2)
print(result)

