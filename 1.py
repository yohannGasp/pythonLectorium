#!/usr/bin/python3

def avg(*args):
	sum = 0.0
	for arg in args:
		sum += arg
	return sum / len(args)

def kargs(fa, **kwargs):
	print(fa)
	for key in kwargs:
		print(key, kwargs[key])

print(avg(1,2))
print(kargs(fa=1,f1="one",f2="two"))

is instance(2,int)

=============================

#!/usr/bin/python3


a,b = 0,1
while b<10:
  print(b)
  a,b = b, a+b

============================
#!/usr/bin/python3

print("Enter")

total = 0;
count = 0;

while True:
	line = input("integer: ")
	if line:
		try:
			number = int(line)
		except ValueError as err:
			print(err)
			continue
		total += number
		count += 1	
	else:
		break

if count:
	print("count= ", count, "total =", total, "mean =", total / count)		
=============================================
#!/usr/bin/python3

def ShowMessage(msg):
    '''message func''' #docstring
    print("-----------------------------------------------------------")
    print(msg)      
    print("-----------------------------------------------------------")

sdf = ShowMessage
sdf("123")

print(ShowMessage.__doc__)
ShowMessage("Enter")

total = 0;
count = 0;

while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1		
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break

if count:
    ShowMessage("count = " + str(count) + " total = " + str(total) + " mean = " + str(total / count))
===========================================
zam
#!/usr/bin/python3

def sky(n):
	def asd(x):
		return n + x
	return asd

as1 = sky(10)
print(as1(5))
=============================




	
