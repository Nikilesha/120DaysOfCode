print("Welcome to tip calculator")

bill = int(input("Enter the bill amount: "))
tip = int(input("Enter the tip percentage you would want to give ? 10 12 15: "))
people = int(input("Enter the number of people: "))
total_tip = tip/100
total_amt = total_tip+bill
bill_per_person = total_amt / people
final = round(bill_per_person,2)
print(f"Each person should pay {final}.")