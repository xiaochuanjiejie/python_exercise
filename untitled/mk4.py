#coding: utf-8

import os

with open('a.ini') as t1,open('b.txt') as t2:
    f1 = t1.readlines()
    f2 = t2.readlines()

for item in f1:
    if item in f2:
        #方法1：
        #用变量名称item导入模块，需用到__import__，模块导入后随即被执行。
        __import__(item.strip())
        #方法2：
        os.system('python %s.py' % item.strip())
        #方法3：
        execfile('%s.py' % item.strip())
    else:
        print '%s not in b.txt' % item.strip()