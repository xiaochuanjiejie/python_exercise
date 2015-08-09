__author__ = 'chuan'

def min1(*args):
    res = args[0]
    for i in args[1:]:
        if i < res:
            res = i
    return res

print min1(2,3,1,'a')