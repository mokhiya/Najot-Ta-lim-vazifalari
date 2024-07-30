# 2. Ikkia list yarating, 
# birinchi listni ichidagi hamma elementlar ikkinchi listni ichida bormi yo'qmi tekshiring

def checking_duplication(list_one: list, list_two: list) -> str:

    """
    The function compares two lists and returns existing and non-existing items.

    params:
    - list_one: list
    -list_two: list
    return:
    - string
    """


    list_one_set = set(list_one)
    list_two_set = set(list_two)

    common_items = list_one_set.intersection(list_two_set) #finding common items in list one and list two
    unique_items_in_list_one = list_one_set - list_two_set #finding left items
    
    # checking wheter all items in list one corresponds with a second one
    if list_one_set == list_two_set:
        return "all items excist in the first list, yay"
    
    else:
        return f"excisting items: {common_items}, left items: {unique_items_in_list_one}"


# test1
user_list_one = ["banana", "guitar", "apple", "toy", "chocolate"]
user_list_two = ["banana", "guittar", "applle", "ttoy", "chocolate"]

print(checking_duplication(user_list_one, user_list_two))

# test2
user_list_one = ["banana", "guitar", "apple", "toy", "chocolate"]
user_list_two = ["banana", "guitar", "apple", "toy", "chocolate"]

print(checking_duplication(user_list_one, user_list_two))