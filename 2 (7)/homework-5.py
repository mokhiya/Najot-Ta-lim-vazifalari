today = int(input("1 dan 7 gacha son kiriting, sizga bugun haftaning qaysi kuni ekanligini aytaman: "))
day_after = int(input("Istalgan sonni kiriting, qaysi hafta kuniga tog'ri kelishini aytaman: "))

if today == 1:
    print("Bugun dushanba")
elif today == 2:
    print("Bugun seshanba")
elif today == 3:
    print("Bugun chorshanba")
elif today == 4:
    print("Bugun payshanba")
elif today == 5:
    print("Bugun juma")
elif today == 6:
    print("Bugun shanba")
else:
    print("Bugun yakshanba")

answer = (today + day_after-1) % 7 + 1
if answer == 1:
    print(f"{day_after} kundan keyin dushanba")
elif answer == 2:
    print(f"{day_after} kundan keyin seshanba")
elif answer == 3:
    print(f"{day_after} kundan keyin chorshanba")
elif answer == 4:
    print(f"{day_after} kundan keyin payshanba")
elif answer == 5:
    print(f"{day_after} kundan keyin juma")
elif answer == 6:
    print(f"{day_after} kundan keyin shanba")
else:
    print(f"{day_after} kundan keyin yakshanba")