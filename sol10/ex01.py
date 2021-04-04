import random

pc_pick = random.randint(1, 100)
my_pick = 0

while (1):
    my_pick = int(input("Guess What? : "))
    if my_pick > pc_pick:
        print("Your guess is bigger than answer")
    elif my_pick < pc_pick:
        print("Your guess is smaller than answer")
    else:
        print("Correct! Well Done :)")
        break