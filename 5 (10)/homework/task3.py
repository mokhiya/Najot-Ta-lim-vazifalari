#1 dan 1000 oralig`idagi 5 ta bo`luvchilari bor sonlarni toping

for num in range(1, 1001):
    divisor = []
    
    for n in range(1, num + 1):  
        
        if num % n == 0:      #if a num is divisible by another number without a residue number 
            divisor.append(n)  #then we are adding that list to a list
    
    if len(divisor) == 5:   #measuring divisor's length
        print(num)
        