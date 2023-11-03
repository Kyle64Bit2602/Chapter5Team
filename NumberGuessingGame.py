import random
import math
import turtle

# Number Guessing Game #
# Main Functions #
default_range = range(1, 1000)

start = 1
set_range = 2
exit_program = 3
def main():
    # Set choice to 0
    choice = 0
    while choice != exit_program:
        menu()
        choice = int(input('Select a choice:'))
        if choice == start:
            guess_(default_range)
  

# Secondary Functions #
def menu():
    # Menu accepts no arguments
    # User has three choices: Start game, range, and exit the program.
    print('MENU\n----')
    print('1) Start Game')
    print('2) Set Range')
    print('3) Exit')
def user_name():
    # User_name accepts no arguments
    # Users input their first names
    # Program returns them
def randomize(min, max):
    # Randomize accepts two arguments
    # Uses the arguments min and max to determine a range for a random number
def guess(num):
    # Guess accepts one argument
    # Guess calls randomize and uses the random integer to determine a number
    # User inputs their own number and the random integer and user's number are compared
