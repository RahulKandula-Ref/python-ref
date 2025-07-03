# game starts here
import sys
import random
from enum import Enum

class RPS(Enum) :
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

keepPlaying = True

while keepPlaying:

    playerchoice = input('Enter ... \n1 for Rock,\n2 for paper,\nAnd 3 for scissors:\n\n')
    player = int(playerchoice)
    if player < 1 or player > 3:
        sys.exit('<<OUT OF RANGE>>')

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
    keepPlaying = bool(int(input('\nKeep Playing? \n 1 or 0!\n\n')))
else:
    print('Sare BYEE!!!')
