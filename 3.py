#!/usr/bin/python3

args = *args

for arg in args:
  try:
    f = open(arg,'r')
  except IOError:
    print("exc " + arg)
  else:
    print(arg + " ok")
  finally
    f.close()
    
  
raise NameError('HiThere')
        


#except (RuntimeError, TypeError):
#  pass

====================================

#!/usr/bin/python3

with open("/etc/passwd") as f:
  for line in f:
    print(line)
  f.close()
  
  
