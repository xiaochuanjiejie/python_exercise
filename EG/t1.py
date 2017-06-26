# -*- coding: UTF-8 -*-
__author__ = 'chuan'
#输入123456789，从第二个数字开始+1，转化为：134567890
import textwrap,string
#方法一：输入int，但实际输出的是str，最终输出的是str
a = raw_input('input num: ')
print type(a)
b = []
c = list(a)
for i in range(1,len(c)):
    if int(c[i]) == 9:
        e = '0'
    else:
        e = str(int(c[i])+1)
    b.append(e)
d = "".join(b)
print c[0] + d
#方法二：输入的是int，输出的是str，但最终输出的还是str
r = input('Input(eg:1234567890): ')
print type(r)
t = str(r)
y = list(t)
u = []
for o in range(1,len(y)):
    if int(y[o]) == 9:
        p = '0'
    else:
        p = str(int(y[o])+1)
    u.append(p)
l = "".join(u)
print y[0] + l