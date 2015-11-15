#!/usr/bin/python3

class Counter:
  count = 0
  def __init__(self):
    print(self.__class__)
    print(self.__name__)
    print(self.__module__)
    print(self.__doc__)
    print(self.__bases__)
    print(self.__dict__)
    
c = Counter()
    
