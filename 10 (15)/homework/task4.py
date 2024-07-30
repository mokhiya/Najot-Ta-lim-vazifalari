# Ikkita ro'yxat yarating va ularni ichida usernamelar yozilgan, 
# vazifangiz ikkala inson (list) uchun ham umumiy bo'lgan foydalanuvchilarni topish
# ya'ni Sizda ikkita foydalanuvchini followerlarini usernamelarini listi bor, 
# ularni o'zingiz yaratasiz. 
# Ikkalasi uchun umumiy bo'lgan usernamelarni topasiz

def common_followers(followers_list_one: list, followers_list_two: list) -> str:
    
    """
    The function finds common followers between two lists.

    params:
    - followers_list_one: list
    - followers_list_two: list
    return:
    - string
    """

    followers_set_one = set(followers_list_one)
    followers_set_two = set(followers_list_two)

    similar_followers_set = followers_set_one.intersection(followers_list_two) # checking if there are similar usernames
    
    if similar_followers_set: # if result is true, it prints common usernames
        return f"Common usernames are: {similar_followers_set}"
    else: #if it is an empty set, it prints a message below
        return "there are no common usernames"


#test 1
first_persons_followers = ["Malika", "Akmal", "Kamol", "Ali"]
second_persons_followers = ["Anvar", "Akmal", "Ali", "Sardor"]

print(common_followers(first_persons_followers, second_persons_followers))


#test 2
first_persons_followers = ["Malika", "Akmal", "Kamol", "Ali"]
second_persons_followers = ["Anvar", "Sardor"]

print(common_followers(first_persons_followers, second_persons_followers))