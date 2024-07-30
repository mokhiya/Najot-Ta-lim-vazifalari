# 1. Ichida 10 element bor list yarating va uni ichida duplicate larini olib tashlang 

def remove_duplicate_items(users_list: list) -> set:
    
    """
    This function removes duplicates from the input list and returns a set of unique items.

    params:
    - list: string
    return:
    - set
    """

    print("Let's creat a ten-item list together. If there are duplicates, I will remove them.")
    
    # creating 10 spaces for a user's input
    for i in range(10):
        users_input = input(f"please, eneter {i + 1}-item: ")
        users_list.append(users_input)
            
    unique_itmes = set(users_list)
    
    print(f"your list: {users_list}")
    return  unique_itmes


your_list = []
print(f"your duplication-free list: {remove_duplicate_items(your_list)}")