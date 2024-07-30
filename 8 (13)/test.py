a_list=[1,5,6,14,85,17,15,30,24,144,174,25]
b_list=[]
count1=0
for arifmet in a_list:
    count1+=arifmet
count2=count1//12
print(count2)

a_list[4]=count2

print(a_list)
