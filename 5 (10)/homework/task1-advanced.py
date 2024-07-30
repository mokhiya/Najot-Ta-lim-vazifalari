number = input("Enter a natural number: ")

#we are collecting unique numbers with a set function
#and looping each unique number
for digit in set(number):

    #we are counting each looped unique number in a user's number 
    counter = number.count(digit)
    print(f"{digit} occures {counter} time(s)")


#dear teacher Kudratbekh, i myself writing all these commentaries 
# to explain you that i understand how it works. 
# please, note it!