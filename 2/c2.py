#!/usr/bin/python3

def info1(self):
  return self.__class__.__name + " " + str(self.__year)
  

class Student:
  city = "St.Peterburg"
  info1 = info1
  
  def __init__(self, name, year):
    self.__name = name
    self.__year = year
    
  def info(self):
    return self.name + " " + str(self.year)
    
  def __del__(self):
    pass    
    
        
st = Student("John", 25)

print(st.city)
print(st.info1())
    
        
    

