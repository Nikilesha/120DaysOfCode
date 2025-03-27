import json

try:
    with open("demo.json","r") as file:
        data  = json.load(file)

        for items in data.keys():
            if items == "age":
                data["age"] += 5
            
except Exception as e:
    print(e)



print(data)

