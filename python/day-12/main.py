import random
from functions import *



print("\nWelcome to the Number guessing game!")
print("I'm thinking of a number between 1 and 100")

level = input("Choose a level : Type 'Easy' or 'Hard': ")

if level.lower() == "easy":
    chances = 10
else:
    chances = 5


number = number_guess()
on = True
while on:
    
    print("\nYou have ",chances," chance(s)")

    guess = int(input("Make a guess: "))

    if chances == 0:
        print("You lost")
        on = False
    elif guess == number:
        print("You Guessed it Right!!")
        on = False
    elif guess < number:
        print("Low")
        chances -= 1
    else:
        print("High")
        chances -= 1