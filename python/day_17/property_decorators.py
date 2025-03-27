"""
class Student:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        if len(new_name)<=0 :
            raise ValueError("Enter a valid name")
        self._name = new_name
        
try:
    no1 = Student("")
except Exception as e:
    print(e)"
"""

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self,new_balance):
        if new_balance < 0:
            raise ValueError("Enter amount greater than 0")
        self._balance = new_balance

    @balance.deleter
    def balance(self):
        self._balance = 0
        print("Balance is set to 0")

account = BankAccount(100)
try:
    account.balance = -50
except Exception as e:
    print(e)
    