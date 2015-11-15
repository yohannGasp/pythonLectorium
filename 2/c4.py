#!/usr/bin/python3

class A:
  def __init__(self, name):
    self.name = name
  def info(self):
    print(self.name)

class B(A):
  def __init__(self,l,name):
    A.__init__(self,name)
    self.l = l
  def info(self):
    print(self.name + " " + self.l)    
        

a=A("John")
a.info()

b=B("lim","John")
b.info()



    
    
    
    
