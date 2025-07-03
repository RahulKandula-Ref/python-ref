# game starts here
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def play_rps():
    playerchoice = input('Enter ... \n1 for Rock,\n2 for paper,\nAnd 3 for scissors:\n\n')
    if playerchoice not in {"1", "2", "3"}:
        print('Unrecognized input. Try again!')
        return play_rps()
    player = int(playerchoice)
    
    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print('You chose : ' + str(RPS(player)).replace('RPS.','').title()
        + ' and python chose : '  + str(RPS(computer)).replace('RPS.','').title())

    # game rules
    if player == 1 and computer == 3:
        print('🎉 You win! 🍾')
    elif player == 2 and computer == 1:
        print('🎉 You win! 🍾')
    elif player == 3 and computer == 2:
        print('🎉 You win! 🍾')
    elif player == computer:
        print('😮 Tie game 😱')
    else:
        print('🐍 Python wins! 🐍')

    # game loop
    if bool(int(input('\nKeep Playing? \n 1 or 0!\n\n'))):
        return play_rps()
    else:
        return "bye"
# play_rps method ends here


# start the game
print(play_rps())