import random
import math
import turtle

# Number Guessing Game #
# Main Functions #
def main():
    pass
    
# Secondary Functions #
def menu():
    # Menu accepts no arguments
    # User has three choices: Start game, range, and exit the program.
    
    pass
def user_name():
    # User_name accepts no arguments
    # Users input their first names
    # Program returns them
    
    #Ask for the names of players
    name1 = input('Please enter a name for player 1: ')
    name2 = input('Please enter a name for player 2: ')
    
    return name1, name2
    
def randomize(min, max):
    # Randomize accepts two arguments
    # Uses the arguments min and max to determine a range for a random number
    
    num = random.randint(min, max)
    
    return num
    
def guess(num, name1, name2):
    # Guess accepts one argument
    # Guess calls randomize and uses the random integer to determine a number
    # User inputs their own number and the random integer and user's number are compared
    
    #Initalize loop
    guess1 = 0
    guess2 = 0
    
    while num != guess1 or num != guess2:
        print(name1, ', guess your number', sep='', end='')
        guess1 = int(input(': '))
        print('Better luck next time.')
        print()
            
        if num == guess1 and num != guess2:
            print('Congrats!', name1, 'Has won!')
        else:
            if guess1!= num and guess2 != num:
                print(name2, ', guess your number', sep='', end='')				#loops after finished
                guess2 = int(input(': '))
                print('You tried.')
                print()
    
            elif guess2 == num:
                print('Congrats!', name2, 'Has won!')
        