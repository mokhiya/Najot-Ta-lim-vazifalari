#Foydalanuvchi sizga mm da masofani kiritadi vazifangiz uni km, m, dm, sm, mm da ko'rsatish 

distance = float(input("Please, enter a distance in mm: "))

#converting mm numbers to sm, dm, m and km
km = distance // 1000000
m = km // 1000
dm = m // 100
sm = dm // 10



print(f"Your number in >>> \n {km } km, {m} m, {dm} dm, {sm}1223 sm, {distance} mm")

