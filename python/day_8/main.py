from data import *


on = True
print(logo)


def encrypt(message,shift):
    msg = ""
    for i in message:
        ch = i.isalnum()
        if ch:
            index = data.index(i)
            new_index = (index+shift)%len(data)
            msg = msg + data[new_index]
        else:
            msg = msg + " "
    return msg

def decrypt(message,shift):
    msg = ""
    for i in message:
        ch = i.isalnum()
        if ch:
            index = data.index(i)
            new_index = (index-shift)%len(data)
            msg = msg + data[new_index]
        else:
            msg = msg + " "
    return msg

            

while on:
    check = True
    type = input("Type 'encode' to encrypt , Type 'decode' to decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))
    if type == "encode":
        print("Here's your encoded message: ",encrypt(message,shift))
    elif type == "decode":
        print("Here's your decoded message: ",decrypt(message,shift))
    else:
        print("Enter correctly")
        check = False

    if check:        
        con = input("Type 'yes' if you want to continue again else type 'no': ")
        
        if con.lower() == "no":
            print("GoodBye")
            on = False