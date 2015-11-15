#!/usr/bin/python3

class A(object):
  _x=0
  def __init__(self, x):
    self._x = x
  def __get__(self):
    return self._x
  def __set__(self, value):
      self._x = value


a=A(5)
print(a._x)
a._x=7
print(a._x)


    
    




  