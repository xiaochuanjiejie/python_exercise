#-*- coding: UTF-8 -*-
__author__ = 'chuan'
'''
有多少个三位整数能被17整除?将之输出。
思路：
整数a除以整数17，除得的商为整数而且没有余数，就说a能被17整除，17能整除a。a称为b的倍数，b称为a的约数。
三位整数:
1.  100-999
2.  [1-9][0-9][0-9](xyz)
'''

# # 思路一:
for a in xrange(100,1000):
    if a % 17 == 0:
        print '数字(%s)能被17整除。' % a

# 思路二:
for x in xrange(1,10):
    x1 = str(x)
    for y in xrange(0,10):
        y1 = str(y)
        for z in xrange(0,10):
            z1 = str(z)
            a = x1 + y1 + z1
            if int(a) % 17 == 0:
                print '数字(%s)能被17整除。' % a