# Odamdan ismini kiritishini so'rang 
# va uni ichida inli harflaridan keyin dollar belgisini qo'shib qaytarib bering.
# Masalan: sa$nja$rbe$k 

name = input("Enter a name: ")

for char in "aiueoAIUEO":

    if char in name:
        name = name.replace(char, char + '$') #replacing each vowel with vowel+&

print(name)