# -*- coding: UTF-8 -*-
__author__ = 'chuan'

a = int(input("biangchang: "))
#获取由几个* 边长的棱形
i = 1
j = 1
while i<a+1:
    print ("   "*(a-i)," * "*(2*i-1))

    i = i+1

while j<a+1:
    print ("   "*j," * "*(2*(a-j)-1))
    j = j+1
