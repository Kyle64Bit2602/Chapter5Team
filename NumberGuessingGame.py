import random
import math

# Number Guessing Game #
# Main Functions #
min_r = 1
max_r = 1000

start = 1
set_range = 2
exit_program = 3
def main():

    name1, name2 = user_name()

    # Set choice to 0
    choice = 0
    while choice == 0:
        menu()
        choice = int(input('Select a choice:'))
        if choice == start:
            guess(default_range, name1, name2)
            choice = int(input('Select a choice:'))
        elif choice == set_range:
            set_range()
            choice = int(input('Select a choice:'))
        elif choice == exit_program:
            print('Thank you for playing the guessing game.')
        else:
            choice = int(input('Please enter a valid number: '))

    
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
    
    #Ask for the names of players
    name1 = input('Please enter a name for player 1: ')
    name2 = input('Please enter a name for player 2: ')
    
    return name1, name2
    
def set_range():
    # Set range accepts no arguments
    # User inputs 2 values to change the range for the guessing game
    # Program returns them
    
    min_r = int(input('Please enter a minimum value for your range: '))
    
    while min_r <= 0:
        min_r = int(input('Please enter a valid number: '))
    max_r = int(input('Please enter a maximum value for your range: '))
    
    while max_r <= 0:
       max_r = int(input('Please enter a valid number: '))
        
    return min_r, max_r
  
def guess(num, name1, name2):
    # Guess accepts one argument
    # Guess calls randomize and uses the random integer to determine a number
    # User inputs their own number and the random integer and user's number are compared
    
    #Initalize loop
    guess1 = 0
    guess2 = 0
    
    while num != guess1 and num != guess2:
        print(name1, ', guess your number', sep='', end='')
        guess1 = int(input(': '))
        
        if num == guess1 and num != guess2:
            print('Congrats!', name1, 'Has won!')
            
        else:
            print('Better luck next time.')
            print()
            
            if guess1 != num and guess2 != num:
                print(name2, ', guess your number', sep='', end='')
                guess2 = int(input(': '))
                 
                if guess2 == num:
                    print('Congrats!', name2, 'Has won!')

                else:
                    print('You tried.')
                    print()

        