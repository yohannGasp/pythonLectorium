#!/usr/bin/python3

def fib(n):
  a,b = 0,1
  while b<10:
    print(b)
    a,b = b, a+b

if __name__ == "__main__":
  fib(10)
