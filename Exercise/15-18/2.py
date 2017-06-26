#-*- coding: utf-8 -*-

class Foo(object):
    '''
    带括号，继承自object，是新式类；要常用新式类
    '''
    pass
class Foo2:
    '''
    不带括号，不继承自object，是经典类
    '''
    pass

p = Foo()
Foo.z = 20
p.x = 7
p.y = 8
print Foo.z,p.x,p.y
print p.z   #p继承了Foo class的属性