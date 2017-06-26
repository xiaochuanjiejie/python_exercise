#-*- coding: utf-8 -*-

class Foo(tuple):

    def __new__(cls,a,b):
        return super(Foo,cls).__new__(cls,tuple((a,b)))
        # print tmp,'---',type(tmp)


    def __init__(self,a,b):
        super(Foo,self).__init__(a,b)
        self.x = a
        self.y = b

p = Foo(3,[5,'a'])
print p
print p.x
print p.y