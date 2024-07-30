#sikl boshlanmoqda
while True:
    #foydalanuvchidan so'z kiritishi so'ralmoqda
    word = input("so'z kiriting: ")

    #agar kiritilgan so'z "exit" so'ziga teng kelmasa
    #kiritilgan so'z uzunligi chop etiladi
    #sikl to'xtaydi
    if word != "exit":
        print(len(word))
        break
    else:
        #agar kiritilgan so'z "exit" so'ziga teng kelsa
        #foydalanuvchiga sikl to'xtagani haqida xabar chiqadi
        #sikl to'xtaydi
        print("exit so'zi kiritildi, sikl to'xtadi")
        break