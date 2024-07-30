import random

words = ("rock", "scissors", "paper")
counter_human = 0
counter_comp = 0
while True:
    
    y = random.choice(words)

    word = input("Your choice: ")
    
    if y == "rock" and word == "rock" or y == "scissors" and word == "scissors" or y == "paper" and word == "paper" :
        print("next round")
        continue
    elif y == "rock" and word == "scissors":
        counter_comp += 1
        print(f"human: {counter_human} : computer {counter_comp}")
        
    elif y == "scissors" and word == "rock":
        counter_human += 1
        print(f"human: {counter_human} : computer {counter_comp}")

    elif y == "rock" and word == "paper":
        counter_human += 1
        print(f"human: {counter_human} : computer {counter_comp}")

    elif y == "paper" and word == "rock":
        counter_comp += 1
        print(f"human: {counter_human} : computer {counter_comp}")

    elif y == "scissors" and word == "paper":
        counter_comp += 1
        print(f"human: {counter_human} : computer {counter_comp}")

    elif y == "paper" and word == "scissors":
        counter_human += 1
        print(f"human: {counter_human} : computer {counter_comp}")
        
    if counter_human == 3:
        print("You won")
    elif counter_comp == 3:
        print("Computer won")


