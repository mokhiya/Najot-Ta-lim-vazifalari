print("Multiplication table: \n")

for number in range(1, 10):
    print(f"""
multilication for {number} 
""")
    
    for n in range(1, 10):
        result = number * n
        
        print(f"{number} * {n} = {result}")
