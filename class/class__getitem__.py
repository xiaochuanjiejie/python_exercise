# -*- coding: UTF-8 -*-
__author__ = 'chuan'

# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             # print x
#             a, b = b, a + b
#         return a
#
# f = Fib()
# print f[4]

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib()
#f后面必须以f[0:5]或f[5]的形式存在，才能将0:5以n的形式传给isinstance(n,slice/int)来进行判断是int还是切片
print f[:10]