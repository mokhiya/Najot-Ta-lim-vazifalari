#foydalanuvchining ismi so'ralmoqda
name = input("ismingizni kiriting: ")

#sikl boshlanmoqda
while True:
    #foydalanuvchi ismi bo'sh satr bo'lmasa
    #va uning uzunligi 0 dan katta bo'lsa
    if name != "" and len(name) > 0:
        #shart bajariladi va foydalanuvchiga ismi bilan xabar chiqadi
        #sikl ishlashdan to'xtaydi
        print("Xush kelibsiz, " + name)
        break
    else:
        #agar ism bo'sh satrga teng bo'lsa
        #yoki enter bosib yuborilgan bo'lsa
        #qayta ism so'ralmoqda
        print("Iltimos, ismingizni kiriting: ")
        name = input()