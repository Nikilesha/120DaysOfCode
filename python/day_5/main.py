import random
alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']


password=[]

print("Welcome to PyPassword Generator")
lett = int(input("Enter how many letters you want in your password: "))
sym = int(input("How many Symbols you'd like: "))
num = int(input("How many numbers you'd like: "))

for _ in range(lett):
    password.append(random.choice(alphabets))


for _ in range(sym):
    password.append(random.choice(symbols))


for _ in range(num):
    password.append(random.choice(numbers))

random.shuffle(password)

print("".join(password))