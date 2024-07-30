# Sizda ikkita ismlar ro'yxati bor, biri choy uchun, ikkinchisi cofe uchun ro'yxatda turibdi, 
# odam sizga ismini kiritadi va 
# sizning vazifangiz u ikkala ro'yxatda ham bormi yo'qmi tekshirish

def name_checking(people_for_tea: list, people_for_coffe: list, users_name: str) -> str:
    """
    The function compares two lists and checks if user_name exists in either list.

    params:
    - people_for_tea: list
    - people_for_tea: list
    - users_name: string
    return:
    - string
    """

    people_for_tea_set = set(people_for_tea)
    people_for_coffe_set = set(people_for_coffe)

    # checking if the name excists in either list
    if users_name in people_for_tea_set and users_name in people_for_coffe_set:
        return "Your name excists in both lists"
    elif users_name in people_for_coffe_set:
        return "Your name excist only in 'people for coffe' list"
    elif users_name in people_for_tea_set:
        return "Your name excist only in 'people for tea' list"
    else:
        return "Your name does not excists in neither list"

poeple_for_tea = ["Malika", "Akmal", "Jamshid"]
poeple_for_coffe = ["Malika", "Otabek", "Akmal", "Murod"]
your_name = input("Please, eneter your name to check in which list your name is: ")

print(name_checking(poeple_for_tea, poeple_for_coffe, your_name))

