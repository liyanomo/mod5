
import json

list1 = {}
with open ('l.json', 'w') as file:
    json.dump(list1,file)
    
class model:
    
    title = input ()
    text = input ()
    author = input ()
 
    def save( ):
        with open('l.json', 'r') as file:
        l = json.load(file)
        reg[log] = password
        with open ("reg.json", "w") as file:
            json.dump(reg,file)
        