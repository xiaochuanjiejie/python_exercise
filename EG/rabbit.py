# -*- coding: UTF-8 -*-
__author__ = 'chuan'

a = 1
b = 1
for i in range(1,21,2):
     # print '**%s**' % i,
     #此print末尾的","符号可使输出数据并列一行
     print '%d %d'%(a,b),
     a += b
     b += a

#分析:
#month	1	2	3	4	5	6	7	8	9	10
#total	1	1	2	3	5	8	13	21	34	55
#此问题是Fibonacci数列问题, f(n) = f(n-1) + f(n-2)