#-*- coding: utf-8 -*-
from functools import partial

'''
1:
偏函数应用指的是固化函数的一个或一些参数，从而产生一个新的函数。
Currying指的是将一个具有多个参数的函数，转换成能够通过一系列的函数链式调用，其中每一个函数都只有一个参数。
'''
#偏函数
def int2(x):
    return int(x,base=2)
print int2('10')

int2 = partial(int,base=2)
print int2('10')

print '分割...'

def max2(x):
    return max(x,5,6,7)
print max2('10')

max2 = partial(max,10)
print max2(5,6,11)

#Currying
def log(level):
    def logMessage(message):
        print level + ": " + message
    return logMessage
#usage
log("Warning")("this is one warning message")
#or like this
logError = log("Error")
logError("this is one error message")
