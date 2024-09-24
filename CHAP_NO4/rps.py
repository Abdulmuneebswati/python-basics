import sys
import random
from enum import Enum

# value = int(input("Please enter your number: "))

# # Now you can compare the integer value
# if value < 5:
#     print("less than 5")
# elif 5 <= value <= 10:
#     print("less than and equal to 10")
# else:
#     print("greater than 10")



class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = int(random.choice("123"))

print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computerchoice)).replace('RPS.', '') + ".")

if player == 1 and computerchoice == 3:
    print("🎉 You win!")
elif player == 2 and computerchoice == 1:
    print("🎉 You win!")
elif player == 3 and computerchoice == 2:
    print("🎉 You win!")
elif player == computerchoice:
    print("😲 Tie game!")
else:
    print("🐍 Python wins!")