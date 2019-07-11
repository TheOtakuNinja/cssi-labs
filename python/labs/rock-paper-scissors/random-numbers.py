
import random

print("dice roller")

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

sum = dice1 + dice2

if dice1 == dice2:
    print("move %d spaces" %(sum))
    print("roll again")
else:
    print("move %d spaces" %(sum))
    print("Next player's turn")
