import json

list1 = {}
with open ('l.json', 'w') as file:
    json.dump(list1,file)
    
class model:
    
    def _init_( self, title, text, author):
        self.title = title 
        self.text = text
        self.author = author
        self.list1 = list1
        self.slv = slv

 
    def save(self):
            slv = {}
            slv.append (text)
            slv.append(author)
            list1[title] = slv
            l1 = json.dump(list1._dict_)
            return (l1)
            
        
while True:
    avt = input ('ввести текст ?')
    if avt == 'да':
            title = input ("введите заголовок:")
            text = input ("введите текст:")
            author = input ("введите автора:")
            print (save(self))
    else:
        break
