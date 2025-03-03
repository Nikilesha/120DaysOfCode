from data import *


print(logo)

def Addition(n1,n2):
    return n1+n2


def Subtraction(n1,n2):
    return n1-n2

def Multiply(n1,n2):
    return n1*n2

def Division(n1,n2):
    return n1/n2


on = True
num1 = float(input("Enter number 1: "))
while on:
    operations={
        "+": Addition,
        "-": Subtraction,
        "*": Multiply,
        "/": Division
    }

    for i in operations:
        print(i)
    operation = input("Pick an operation: ")
    num2 = float(input("Enter number 2: "))
    answer = operations[operation](num1,num2)
    print(f"{num1} {operation} {num2} = {answer}")
    choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation:  ").lower()
    if choice == 'y':
        num1= answer
    else:
        on = False