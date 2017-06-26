#-*- coding: utf-8 -*-

class Foo(object):
    num = 5
    def __init__(self,x,y):     #构造函数
        self.x = x
        self.y = y
    def print_xy(self):
        print self.x,self.y

p = Foo(3,7)
p.print_xy()