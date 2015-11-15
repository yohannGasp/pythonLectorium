#!/usr/bin/python3

#decorator

def makebold(fn):
	def wrapped():
		return "<b>" + fn() + "</b>"
	return wrapped

@makebold
def hello():
	return "hello world"

print(hello())


===============================

#!/usr/bin/python3

#decorator

def makebold():
	def wrapped():
		return "<b>123</b>"
	return wrapped

print(makebold()())



# func parametr
def doSome(func):
	print("123123123")
	print(func())

doSome(sum())	

=======================================

#!/usr/bin/python3

for el in [1,2,3]:
    print(el)

for el in (1,2,3):
    print(el) 

for key in {'one':1,'two':2}:
    print(key)

for char in "123":
    print(char)

for line in open("/etc/passwd"):
    print(line)

========================================

#!/usr/bin/python3

#s = "ab"
#it = iter(s)
#print(it)
#it.next()
#it.next()

# iterator
class Reverse(object):
	"""docstring for Reverse"""
	def __init__(self, data):
		self.data = data
		self.index = len(data)
	def __iter__(self):
		return self
	def next(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]

for char in Reverse('spam'):
    print(char)		

===================================

#!/usr/bin/python3


# generator
def reverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index] # при выходе из функции сохр позицию

for char in reverse('spam'):
    print(char)		

=======================================

#!/usr/bin/python3


# vyr - generators
sum(i*i for i in range(10))

x = [10,20,30]
y = [7,5,3]
sum(x*y for x,y in zip(x,y))

uniq_w = set(word for line in page for word in line.splite())

=======================================





