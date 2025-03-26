import json
class Expense:
    def __init__(self,name,age,email,phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    def add_dict_user(self):
        return(
            {
                "name" : self.name,
                "age" : self.age,
                "email": self.email,
                "phone": self.phone
            }
        )
    
    def writing_file(self):
        try:
            try:
                with open("demo.json","r") as file:
                    data = json.load(file)
            except Exception as e:
                data = []
            
            data.append(self.add_dict_user())

            with open("demo.json","w") as file:
                json.dump(data,file,indent=4)
            print("data added to json")
            

        except Exception as e:
            print("Error writing the file")


user1 = Expense("Nikilesha",25,"nikilesha20@gmail.com",6374042158)
user2 = Expense("Nick",20,"nikilesh20@gmail.com",6274042158)
user1.writing_file()
user2.writing_file()



                

