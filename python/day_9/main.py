from data import *
import os


print(img)
on  =True
bids={}
while on:
    
    
    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))
    
    bids[name] = bid
    other = input("Are there any other bidders? Type 'Yes' or 'No': ").lower()
    if other == "no":
        
        max_value = max(bids.values())
        for i ,j in bids.items():
            if j == max_value:
                max_person = i
                break;
        print("The Winner is ",max_person,"with a bid of $",max_value)
        on = False
    else:
        os.system('cls')
    