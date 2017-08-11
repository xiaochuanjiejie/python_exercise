#coding: utf-8

import math
from functools import reduce

s = '1234.5678'
index = s.index('.')
n = len(s) - 1 - index
s = s.replace('.','')
print s

def chr2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

print map(chr2num,s)
lst = map(chr2num,s)
# lst = list(map(chr2num,s))
# print lst

def cal(x,y):
    return x * 10 + y

number = reduce(cal,lst)
print number

floatx = number / math.pow(10,n)
print floatx