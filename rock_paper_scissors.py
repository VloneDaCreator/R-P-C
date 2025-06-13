import random
import time

def print_slow(text):
    for letter in text:
        print(letter, end="")
        time.sleep(0.05)
    print("\n")

def game():
    choices = ["rock", "paper", "scissors"]
    
    print_slow("Welcome Traveler, to the game of Rock, Paper, Scissors!")
    print_slow("The challenge you've chosen is simple:")
    print_slow("You will play against the ALMIGHTY COMPUTER!!!")

    while True:
        print_slow("Choose your weapon: rock, paper, or scissors:")
        player_choice = input().strip().lower()
        if player_choice not in choices:
            print_slow("Thy Traveler not know the rules of the game?")
            continue

        print_slow(f"Very well, you chose {player_choice}. Now let's see what the ALMIGHTY COMPUTER chooses...")
        time.sleep(1)
        computer_choice = random.choice(choices)
        print_slow(f"The ALMIGHTY COMPUTER chose {computer_choice}.")

        if player_choice == computer_choice:
            print_slow("It's a TIE! A match made in the HEAVENS!!!")
            continue
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print(r"""
   
  / \
  | |
  |.|
  |.|
  |:|      __
,_|:|_,   /  )
  (Oo    / _I_
   +\ \  || __|
      \ \||___|
        \ /.:.\-\
         |.:. /-----\
         |___|::oOo::|
         /   |:<_T_>:|
        |_____\ ::: /
         | |  \ \:/
         | |   | |
         \ /   | \___
         / |   \_____\
         `-'""")
            print_slow("Thou art VICTORIOUS! The ALMIGHTY COMPUTER is defeated!")
        else:
            print(r"""
             /\
            /  \
           |    |
         --:'''':--
           :'_' :
           _:"":\___
   ' '  ____.' :::     '._
 . *=====<<=)           \    :
  .  '      '-'-'\_      /'._.'
                   \====:_ ""
                  .'     \\
                 :       :
                /   :    \
               :   .      '.
,. _        snd :  : :      :
'-'    ).          :__:-:__.;--'
(        '  )        '-'   '-'
 ( -   .00.   - _
(    .'  _ )     )
'-  ()_.\,\,   -")
""")
            print_slow("Alas! The ALMIGHTY COMPUTER has bested thee. Better luck next time!")

        print_slow("Do you wish to play again, Traveler? (yes/no)")
        play_again = input().lower()
        if play_again != "yes":
            print_slow("Farewell, brave Traveler! Until we meet again!")
            break

if __name__ == "__main__":
    game()
