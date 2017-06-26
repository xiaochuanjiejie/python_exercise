# -*- coding: utf-8 -*-
__author__ = 'chuan'

dict1 = {1:"a",2:"b","c":3}

#字典排序方法一
def sort1(adict):
    a = adict.items()
    a.sort()
    return [value1 for key1,value1 in a]

print sort1(dict1)
#字典排序方法二
def sort2(bdict):
    b = bdict.keys()
    b.sort()
    return [bdict[key2] for key2 in b]
print sort2(dict1)