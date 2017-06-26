#-*- coding: utf-8 -*-

class Foo(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def test(self):
        print 'in 父类'

class Foo2(Foo):
    def __init__(self,x,y,z):
        print '调用子类自己的构造函数'
        # Foo.__init__(self,x,y)      //缺陷是若父类名称变化，调用失效，可用下行方法
        super(Foo2,self).__init__(x,y)
        self.z = z
    def test(self):
        print self.x,self.y,self.z
        print 'in 子类'


p = Foo2(4,5,6)
print '---'
p.test()