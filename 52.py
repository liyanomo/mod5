import json

list1 = {}
with open ('l.json', 'w') as file:
    json.dump(list1,file)
    
class Model:

    title = 1
    text = 2
    author = 3
    
    def _init_( self, title, text, author):
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
        self.l = json.dump(list1._dict_)
        return (self.l)
            
s = Model()
s.save1 (self.l)
print (s.save1)