'''
Lucio
Febuary 14, 2022
This code will make a dice game.
'''

from random import randint #Imports libraries
from time import sleep

budget = 100 #Starting budget of 100

def roll_dice(wager, budget): #Function to roll the dice
    first_roll = randint(1, 6)
    second_roll = randint(1, 6)
    total = first_roll + second_roll
    sleep(1)
    
    print("Rolling...")
    sleep(2)
    print("House first roll is " + str(first_roll) + ".")
    sleep(1)
    print("House second roll is " + str(second_roll) + ".")
    sleep(1)
    print("House roll is " + str(total) + ".")
    sleep(1)
        
    if user_guess == total: #Win or lose
        wager = wager * 12
        print("You won!")
        return wager
    
    else:
        print("You lost!")
        return -wager
    
print("Hello, welcome to the casino!") #Welcome message

while budget > 0: #loop game
    choice = input("Would you like to play this dice game, Yes or No? ")
    
    if choice == "No":
        print("Okay! Hope to see you back soon!")
        break
    
    else:
        print("From your budget of " + str(budget) + ", wager.")
        wager = int(input("How much would you like to wager: "))
        
        if wager > budget or wager < 1:
            print("Insufficient wager!")
            break
        
        else:
            print("Now let's begin the game!")
            user_guess = int(input("Guess a number between 2 and 12: "))
        
            if user_guess > 12 or user_guess < 2:
                print("Invalid guess!")
                break
    
            else:
                budget = budget + roll_dice(wager, budget)
                print("You are walking away with a budget of " + str(budget) + ".")