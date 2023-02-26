511.py
class StringVar:  
    def __init__(self, number = 0):  
         self._number = number
    def set_number(self, a):  
        self._number = a 
    def get_number(self):  
        return self._number  
   
s = StringVar()  
s.set_number("номер 14")  
print(s.get_number()) 
print(s._number) 
