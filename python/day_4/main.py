#Rock Paper Scissors
import random
from image import *
items = [rock,paper,scissors]

choice = int(input("What do you choose ? Type 0 for rock , 1 for Paper , 2 for Scissors.\n"))

if choice >0 or choice<2:
    print("Your choice: ")
    print(items[choice])
    c_choice = random.randint(0,2)
    print("Computer Choice: \n")
    print(items[c_choice])
else:
    print("Invalid Choice Entered")

if choice == c_choice:
    print("It's a draw")

elif choice == 0 and c_choice ==1:
    print("You Lose")
elif choice == 0 and c_choice == 2:
    print("You Win")

elif choice == 1 and c_choice ==0:
    print("You Win")
elif choice == 1 and c_choice == 2:
    print("You Lose")

elif choice == 2 and c_choice ==0:
    print("You Lose")
elif choice == 2 and c_choice == 1:
    print("You Win")
