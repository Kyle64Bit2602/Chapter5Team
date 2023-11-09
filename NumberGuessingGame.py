import random
import math

# Number Guessing Game #
# Main Functions #



def main():

    name1, name2 = user_name()

    # Set varibles
    min_r = 1
    max_r = 1000
    ran_num = random.randint(min_r, max_r)

    start = 1
    setrange = 2
    choice = menu()
    while choice >= 1 and choice <= 2:
        if choice == start:
            guess(max_r, min_r, ran_num, name1, name2)
        elif choice == setrange:
            min_r, max_r, ran_num = set_range()
        choice = menu()
        
       
    
# Secondary Functions #
def menu():
    # Menu accepts no arguments
    # User has three choices: Start game, range, and exit the program.
    
    print('MENU\n----')
    print('1) Start Game')
    print('2) Set Range')
    print('3) Exit')
    choice = int(input('Select a choice:'))
    return choice

def user_name():
    # User_name accepts no arguments
    # Users input their first names
    # Program returns them
    
    # Ask for the names of players
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
       
    ran_num = random.randint(min_r, max_r)
        
    return min_r, max_r, ran_num
  

def guess(max_r, min_r, num, name1, name2):
    # Guess accepts one argument
    # Guess calls randomize and uses the random integer to determine a number
    # User inputs their own number and the random integer and user's number are compared
    
    # Initalize loop
    guess1 = 0
    guess2 = 0
    
    while num != guess1 and num != guess2:
        print(name1, ', guess your number', sep='', end='')
        guess1 = int(input(': '))
        
        while guess1 > max_r or guess1 < min_r:
            print('Please enter a number between ', max_r, ' and ', min_r, ' .', sep='')
            print(name1, ', guess your number', sep='', end='')
            guess1 = int(input(': '))
        
        if num == guess1 and num != guess2:
            print('Congrats!', name1, 'Has won!')
            print()
            
        else:
            
            if guess2 < num:
                print('Try a higher number.')
                print()
                
            elif guess2 > num:
                print('Try a lower number.')
                print()
                
        if guess1 != num and guess2 != num:
            print(name2, ', guess your number', sep='', end='')
            guess2 = int(input(': '))
            
            while guess1 > max_r or guess1 < min_r:
                print('Please enter a number between ', max_r, ' and ', min_r, ' .', sep='')
                print(name2, ', guess your number', sep='', end='')
                guess2 = int(input(': '))
                
            if guess2 == num:
                print('Congrats!', name2, 'Has won!')
                print()

            else:
                
                if guess2 < num:
                    print('Try a higher number.')
                    print()
        
                elif guess2 > num:
                    print('Try a lower number.')
                    print()
