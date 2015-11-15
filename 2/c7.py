#!/usr/bin/python3

# virtual metod
class Pure(object):
  def pure(self):
    raise NotimplementedError('Metod virtual')
    
Pure().pure()


class Add:
  def __call__(self,x,y):
    return x + y
    
add = Add()
add(3,4)    

    
class oldstyle:
  pass
  
class Newstyle(object):
  pass


class Child(Parent):
  def __init__(self):
    super(Child,self).__init__(self) # constructor predka
    
# property

class A(object):
  def __init__(self, x):
    self._x = x

  def getx(self):
    return self._x

  def setx(self, value):
      self._x = value

  def delx(self):
  	del self._x
x = property(getx, self, delx, "property doc")

#static method

class StExample(object):
	@staticmethod
	def test(x):
		return x == 0
		











    
    




  