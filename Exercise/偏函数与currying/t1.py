#-*- coding: utf-8 -*-
from functools import partial

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