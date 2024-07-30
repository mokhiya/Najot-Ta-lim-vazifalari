
# set_names = {"Malika", "Jasur", "Otabek"}

# users_name = input("Please, enter your name: ")

# if users_name in set_names:
#         print("Your name is already in the list", set_names)
# else:
#     set_names.add(users_name)
#     print(set_names)
import random

def recommending_products(bought_items: list, sailing_items: list) -> str:
    
    set1 = set(bought_items)
    set2 = set(sailing_items)

    remained_items = set2.symmetric_difference(set1)
    
    random_recommendation = random.sample(list(remained_items), 3)
    return random_recommendation


purchased_products = ["apple", "banana", "strawberry"]
products_in_sale = ["blueberry", "strawberry", "orange", "lemon", "apple"]

result = recommending_products(purchased_products, products_in_sale)
print(result)



