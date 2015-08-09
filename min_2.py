__author__ = 'chuan'

def min2(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print min2(4,1,2,3,'a')