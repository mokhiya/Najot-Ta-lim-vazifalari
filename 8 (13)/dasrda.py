# names_list =  []
# for _ in range(10):
#     name = input("enter a name: ")
#     names_list.append(name)

# print(names_list)

# numbers = [1, 2, 3, 4.4, 5, 6.6, 7, 8, 9, 10]

# float_list = []
# integer_list = []

# for i in numbers:
#     if type(i) == float:
#         float_list.append(i)
#     else:
#         integer_list.append(i)

# print(f"floats: {float_list}, itegers: {integer_list}")

# integer_list = [-1, 0, -3, 3, 4, 5, 6, 8, -3, -5, 0, 0, 7, 8, 10]

# counter_negative = 0
# summa = 1
# counter_zero = 0

# for n in integer_list:
#     if n < 0:
#         counter_negative += 1
#     elif n == 0:
#         counter_zero *= 1
#     else:
#         summa += n

# print(f"zero numbers: {counter_zero}, negative numbers: {counter_negative}, sum of positive umbers: {summa}")

# board = [
#     ['-', '-', '-'],
#     ['-', '-', '-'],
#     ['-', '-', '-']
# ]

# attemp = 1

# while attemp <= 9:
#     for row in board:
#         print(board)
    
#     if board[0][0] == "X" and  board[0][1] == "X" and board[0][2] == "X" or\
#     board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" or\
#     board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" or\
#     board[0][0] == "X" and  board[0][1] == "X" and board[0][2] == "X":
#         print("Player A is winner!")
#         break
#     else:
#         pass
#     if attemp % 2 == 1:
#         user_input = int(input("Enter a number for X: "))
#         if user_input == 1:
#             board[0][0] = "X"
#         elif user_input == 2:
#             board[0][1] = "X"
#         elif user_input == 3:
#             board[0][2] = "X"
#         elif user_input == 4:
#             board[1][0] = "X"
#         elif user_input == 5:
#             board[1][1] = "X"
#         elif user_input == 6:
#             board[1][2] = "X"
#         elif user_input == 7:
#             board[2][0] = "X"
#         elif user_input == 8:
#             board[2][1] = "X"
#         elif user_input == 9:
#             board[2][2] = "X"
#     else:
#         user_input = int(input("Enter a number for O: "))
#         if user_input == 1:
#             board[0][0] = "O"
#         elif user_input == 2:
#             board[0][1] = "O"
#         elif user_input == 3:
#             board[0][2] = "O"
#         elif user_input == 4:
#             board[1][0] = "O"
#         elif user_input == 5:
#             board[1][1] = "O"
#         elif user_input == 6:
#             board[1][2] = "O"
#         elif user_input == 7:
#             board[2][0] = "O"
#         elif user_input == 8:
#             board[2][1] = "O"
#         elif user_input == 9:
#             board[2][2] = "O"

    
items = [8, 2, 5, 3, 3]
items = min(items)
print(items)
