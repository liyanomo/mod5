import json

list1 = {}
slv = {}
with open ('l.json', 'w') as file:
    json.dump(list1,file)
    
class Model:

    title = 1
    text = 2
    author = 3
    
    def __init__( self, title, text, author):
        self.title = title 
        self.text = text
        self.author = author
        self.list1 = list1
        self.slv = slv

    @staticmethod
    
    def save1 (self):
        self.slv = {}
        self.slv.append (self.text)
        self.slv.append(self.author)
        self.list1[title] = self.slv
        l.json= json.dump(list1._dict_)
        return (l.json)
            
s = Model('заголовок', 'текст', 'автор')
s.save1(self)
print (s.save1)