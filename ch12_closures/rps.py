# game starts here
import sys
import random
from enum import Enum

def rps_init():

    game_count = 0
    player_wins = 0
    computer_wins = 0

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    def play_rps():

        nonlocal game_count
        nonlocal player_wins
        nonlocal computer_wins


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
                record_player_win()
                return '🎉 You win! 🍾' 
            elif player == 2 and computer == 1:
                record_player_win()
                return '🎉 You win! 🍾' 
            elif player == 3 and computer == 2:
                record_player_win()
                return '🎉 You win! 🍾' 
            elif player == computer:
                update_stats()
                return '😮 Tie game 😱' 
            else:
                record_computer_win()
                return '🐍 Python wins! 🐍' 
            
        def update_stats(player = 0, computer = 0):
            nonlocal game_count
            nonlocal player_wins
            nonlocal computer_wins

            game_count += 1
            player_wins += player
            computer_wins += computer

        def record_player_win():
            update_stats(player=1)
        
        def record_computer_win():
            update_stats(computer=1)

        def print_game_stats():
            print("\nGame count: " + str(game_count))
            print("You win: " + str(player_wins))
            print("You lost: " + str(computer_wins))

        # game loop
        player = input_player_choice()
        computer = computer_choice()
        winner = decide_winner(player, computer)

        print('You chose : ' + str(RPS(player)).replace('RPS.','').title()
            + ' and python chose : '  + str(RPS(computer)).replace('RPS.','').title())
        print(winner)
        print_game_stats()

        if bool(int(input('\nKeep Playing? \n 1 or 0!\n\n'))):
            return play_rps()
        else:
            sys.exit('bye')
        # game loop ends here
    # play_rps method ends here

    return play_rps


# start the game
rps_game = rps_init()
rps_game()