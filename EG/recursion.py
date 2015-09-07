# -*- coding: UTF-8 -*-
__author__ = 'chuan'

#一层嵌套
numList0 = [1,2,3,[4,5,6]]
for i in numList0:
    if isinstance(i,list):
        for j in i:
            print j
    else:
        print i
#两层嵌套
numList1 = [1,2,3,[4,5,6,[7,8,9]]]
for i in numList1:
    if isinstance(i,list):
        for j in i:
            if isinstance(j,list):
                for k in j:
                    print k
            else:
                print j
    else:
        print i
#通过上面两个方法，能够将list中的元素逐个输出，但过于繁琐需写多层嵌套，可以使用recursion（递归），重点在于if后的函数再次使用一节节拔高相当于。
numList2 = [1,2,3,[4,5,6,[7,8,9]]]
def print_item(List):
    for i in List:
        if isinstance(i,list):
            print_item(i)
        else:
            print i
print_item(numList2)