class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def disp(self):
        print(f"Person: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary = salary

    def disp(self):
        super().disp()
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, age, salary,size):
        super().__init__(name, age, salary)
        self.size = size


    def disp(self):
        super().disp()
        print(f"Team Size:{self.size} ")

manager = Manager("alice",35,85000,4)

manager.disp()
        