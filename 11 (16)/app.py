names = {
    "sancho": ["ali", "vali"],
    }
user_name = input("Enter a name: ")

for name in names["sancho"]:
    #print(name)
    if name == user_name:
        print(name)
    else:
        names["new_name"] = user_name

print(names)