# game starts here
import sys
import random
from enum import Enum

game_count = 0

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def play_rps():
    def input_player_choice():
        playerchoice = input('Enter ... \n1 for Rock,\n2 for paper,\nAnd 3 for scissors:\n\n')
        if playerchoice not in {"1", "2", "3"}:
            print('Unrecognized input. Try again!')
            return play_rps()
        return int(playerchoice)
    
    def computer_choice():
        computerchoice = random.choice("123")
        return int(computerchoice)
    
    def decide_winner(player, computer):
        # game rules
        if player == 1 and computer == 3:
            return '🎉 You win! 🍾' 
        elif player == 2 and computer == 1:
            return '🎉 You win! 🍾' 
        elif player == 3 and computer == 2:
            return '🎉 You win! 🍾' 
        elif player == computer:
            return '😮 Tie game 😱' 
        else:
            return '🐍 Python wins! 🐍' 
    

    player = input_player_choice()
    computer = computer_choice()

    print('You chose : ' + str(RPS(player)).replace('RPS.','').title()
        + ' and python chose : '  + str(RPS(computer)).replace('RPS.','').title())

    winner = decide_winner(player, computer)
    print(winner)

    global game_count
    game_count += 1
    print('\nGame count : ' + str(game_count))

    # game loop
    if bool(int(input('\nKeep Playing? \n 1 or 0!\n\n'))):
        return play_rps()
    else:
        sys.exit('bye')
# play_rps method ends here


# start the game
play_rps()