from img import *
import random

def random_number():
    return random.randint(1, 10)

yes = input("Do you want to play the game 'Y' or 'N': ")
if yes.lower() == "y":
    print(logo)
    random_num_user = []
    random_num_computer = []

    for i in range(2):
        random_num_computer.append(random_number())
        random_num_user.append(random_number())
    
    while sum(random_num_computer) < 17:
        random_num_computer.append(random_number())

    while True:
        print("Your Cards:", random_num_user, "Current Score:", sum(random_num_user))
        print("Computer's First Card:", random_num_computer[0])
        
        next_move = input("Type 'Y' to get another card, type 'N' to pass: ")
        if next_move.lower() == "y":
            random_num_user.append(random_number())
            if sum(random_num_user) > 21:
                print("You lose! You went over 21.")
                print("Your Score:", sum(random_num_user))
                print("Computer's Score:", sum(random_num_computer))
                exit()
        elif next_move.lower() == "n":
            break

    print("Final Scores:")
    print("Your Score:", sum(random_num_user))
    print("Computer's Score:", sum(random_num_computer))

    if sum(random_num_computer) > 21 or sum(random_num_user) > sum(random_num_computer):
        print("You Win!")
    elif sum(random_num_user) < sum(random_num_computer):
        print("You Lose!")
    else:
        print("It's a Tie!")
