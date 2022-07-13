


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#
# this is the "game.py" file...

import random

print("Rock, Paper, Scissors, Shoot!")


# USER INPUTS

user_choice = input("Please make a selection ('rock', 'paper', 'scissors):")
user_choice = user_choice.lower()

# You chose: 'rock'
print ("You chose:", user_choice)
print (f"You chose: '{user_choice}' ")

# VALIDATE USER INPUTS

valid_options = ["rock", "paper", "scissors"]


#breakpoint()

# if user_choice in valid_options:
    # NEST ALL THE STUFF INDENTED
    # use the user choice, etc
# else:
    # print("OOPS INVALID TRY AGAIN") 


if user_choice not in valid_options:
    print("OOPS INVALID TRY AGAIN")
    exit() #quit() 

# COMPUTER CHOICE

# import random

# valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)

# DETERMINE THE WINNER

# from code shared in slack by Bonnie: 

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock crushes scissors. You lose.")

    


# DISPLAY RESULTS


# -------------------
# Welcome 'Player One' to my Rock-Paper-Scissors game...
# -------------------
# Please choose either 'rock', 'paper', or 'scissors': rock
# You chose: 'rock'
# The computer chose: 'paper'
# -------------------
# Oh, the computer won. It's ok.
# -------------------
# Thanks for playing. Please play again!