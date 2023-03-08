import json

    
class Model:

    title = 1
    text = 2
    author = 3
    
    def __init__( self, title, text, author):
        self.title = title 
        self.text = text
        self.author = author
    
    def save1 (self):
        d = self.__dict__
        with open ('l.json', 'w') as file:
            json.dump(d,file)
            
s = Model('заголовок', 'текст', 'автор')
s.save1(self.__dict__)
print (s.save1)