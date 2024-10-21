
from enum import Enum
import random
import sys


game_count = 0

def playRps():
    class RPS(Enum):
        Rock=1
        Paper=2
        Scissor=3
    playerChoice = int(input("\n Enter... \n 1 for Rock \n 2 for Paper \n 3 for scissor\n"))

    if (playerChoice not in [1,2,3]):
        print("You must enter 1, 2, or 3.")
        return playRps()
    
    computer_choice = int(random.choice("123"))

    print("you choose " + str(RPS(playerChoice)).replace("RPS.","").title() + ".")
    print("python choose " + str(RPS(computer_choice)).replace("RPS.","").title() + ".")

    def decideWinner(playerChoice,computer_choice):
        print(playerChoice)
        if playerChoice == 1 and computer_choice == 3:
            print("🎉 You win!")
        elif playerChoice == 2 and computer_choice == 1:
            print("🎉 You win!")
        elif playerChoice == 3 and computer_choice == 2:
            print("🎉 You win!")
        elif playerChoice == computer_choice:
            print("😲 Tie game!")
        else:
            print("🐍 Python wins!")


    decideWinner(playerChoice,computer_choice)
    global game_count
    game_count +=1
    print("\nGame Count : " + str(game_count))
    print("\nPlay again?")

    while True:
        playagain = input("\nY for Yes or \nQ to Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break
    
    if playagain.lower() == "y":
        return playRps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")

playRps()

