# For this assignment, write a .sh file called `boot.sh`. In the same directory as boot.sh, 
# create a Python file that plays a game of rock paper scissors. Use boot.sh to ask users 
# if they'd like to play rock paper scissors; if they answer 'yes', then execute the Python 
# file. If not, have the shell file tell users 'That's too bad, maybe next time'.

# It is common to use Shell scripts to boot entire applications; this is a very small version of that same concept.

# The notion document attached comes courtesy of Coding Temple's very own Derek Hawkins and covers similar topics.
# Upload your Python and your shell script to Github, and post the repo link here


import random

# using a while loop to make playing multiple games easier.
while True:
    user_action = input("Please choose rock, paper, or scissors: ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}. The computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock crushes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock crushes scissors! You lose.")

    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() != "y":
        print("That's too bad, maybe next time")
        break