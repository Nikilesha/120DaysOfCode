from image import *

print(img)
on = True
while(on):
    a = input("You're at a cross-road. Where you want to go? \n \t\t Type 'Left' or 'Right'\n")
    if a.lower() == 'right':
        print("\nYou fell into a hole\n Game Over")
        on = False
    elif a.lower() == 'left' :
        b = input("\nYou've come to a lake. There is an island in the middle of the lake.\n\t\tType 'wait' to wait for a boat. Type 'swim' to swim across.\n")
        if b.lower() == 'swim':
            print("\nYou get eaten by a crocodile.\n Game Over")
            on = False
        elif b.lower() == 'wait':
            c = input("\nYou arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue. Which colour do you choose?\n")
            if c.lower()=='red':
                print("\nYou went into a room of fire\nGame Over")
                on = False
            elif c.lower()=='blue':
                print("\nYou went into a room full of water\nGame Over")
                on = False
            elif c.lower() == 'yellow':
                print("\nYou reached safeley\n You Win!!")
                on  = False
            