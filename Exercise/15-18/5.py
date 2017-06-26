#-*- coding: utf-8 -*-

z = 100
class Foo(object):
    num = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def print_x_y(self):
        return self.x + self.y + self.num + z

p = Foo(5,6)
print p.print_x_y()
print p.__class__
print vars(p)