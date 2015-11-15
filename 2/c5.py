#!/usr/bin/python3

class A:
  def info(self):
    print("first")

class B:
  def info(self):
    print("second")    

class C(A,B):
  def info_parent(self):
    self.info()
    
c=C()
c.info_parent()
    
    
