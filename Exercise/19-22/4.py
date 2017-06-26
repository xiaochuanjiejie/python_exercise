#-*- coding: utf-8 -*-

'''
封装和隐藏（私有化），隐藏的方法和变量若不特殊处理不能被继承
'''

class Foo(object):
    __num = 10
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.__c = c
    def print_a_b_c(self):
        print self.a,self.b,self.__c
    def __print_abc(self):
        print self.a,self.b,self.__c


p = Foo(1,2,3)
print p.a,p.b
# print p.__c   //隐藏了不能被显示
print '特殊方法调用隐藏变量： %s' % p._Foo__c
p.print_a_b_c()
print '***'
p._Foo__print_abc()
print '特殊方法调用隐藏变量： %s' % Foo._Foo__num