from hangman_data import *
import random

def random_choice_name():
    return random.choice(hangman_words)

def blank_fill(answer):
    for i in answer:
        print("_",end=" ")

def game():
    on = True
    answer = random_choice_name()
    blank_fill(answer)
    guessed = ["_"]*len(answer)
    print()
    life = 5
    while on:
        print("Lifes: ",life)
        guess = input("Enter your guess: ").lower()
        disp=""
        correct = False
        for i in range(len(answer)):
            if answer[i] == guess:
                guessed[i] = guess
                correct = True
            disp+= guessed[i]

        if not correct:
            life-=1
        print(disp,sep=" ",end="\n",)
        

        if "_" not in guessed:
            print("Congrats you won!!!")
            on = False
        elif life==0:
            print("You lost the word was ",answer)
            on = False

game()
            