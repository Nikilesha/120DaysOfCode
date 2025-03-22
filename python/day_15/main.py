"""
class ToDoList:
    def __init__(self,file_name="to_do_list.txt"):
        self.file_name = file_name
    

    def addTask(self,task):
        try:
            with open(self.file_name,"a") as f:
                f.write(task+"\n")
        except Exception as e:
            print(f"{e}")
        

    def viewTask(self):
        try:
            with open(self.file_name,"r") as f:
                tasks = f.readlines()
                if not tasks:
                    print("No tasks found")
                for i in tasks:
                    print(i,end="\n")
        except Exception as e:
            print(f"{e}")


    def deleteTask(self):
        try:
            open(self.file_name,"w").close()
            print("All deleted")
        except Exception as e:
            print(f"{e}")
    
todo = ToDoList()
todo.addTask("Hello i am nikilesha")
todo.viewTask()
todo.deleteTask()"
"""
import csv

class TodoCsv:
    def __init__(self,file_name="students.csv"):
        self.file_name = file_name

    def add_task(self,name,mark):
        try:
            with open(self.file_name,"a",newline="") as f:
                writer = csv.writer(f)
                writer.writerow([name,mark])
            print("Successfully added")
            
        except Exception as e:
            print(f"{e}")


    def view_task(self):
        try:
            with open(self.file_name,"r") as f:
                reader = csv.reader(f)
                for i in reader:
                    print(i)
        except Exception as e:
            print(f"{e}")
    

manager=  TodoCsv()
manager.add_task("alice",65)
manager.add_task("divya",25)
manager.view_task()