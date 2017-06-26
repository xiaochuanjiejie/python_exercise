#-*- coding: utf-8 -*-

def mult(x,y):
    return x * y
def factorial_0(n):
    return reduce(mult,range(1,n+1))
def factorial_1(n):
    return reduce(lambda x,y:x*y,range(1,n+1))

print factorial_0(5)
print factorial_1(5)