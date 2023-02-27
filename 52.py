import json

list1 = {}
with open ('l.json', 'w') as file:
    json.dump(list1,file)
    
class model:
 
    def save():
        slv = {}
        slv.append (text)
        slv.append(author)
        l[title] = slv
        with open ("l.json", "w") as file:
            json.dump(l,file)
            
        
while True:
    avt = input ('ввести текст ?')
    if avt == 'да':
            title = input ("введите заголовок:")
            text = input ("введите текст:")
            author = input ("введите автора:")
            print (save())
    else:
        break