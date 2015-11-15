#!/usr/bin/python3

class A:
  "class A example"
  attr = 12345
  def foo(self):
    return 'hello'

class B:
  pass
B.b = B()
        
print(A.foo)

a = A()
print(a.__doc__)
print(a.attr)
print(a.foo())


