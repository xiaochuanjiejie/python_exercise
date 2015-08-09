# -*- coding: UTF-8 -*-
__author__ = 'xiaochuanjiejie@outlool.com'

class person:
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay
    def lastname(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay = int(self.pay * (1+percent))
        return self.pay
    #运算符重载（打印重载__str__）
    def __str__(self):
        return '[Person: %s,%s]' % (self.name,self.pay)
#类继承低级方法
class manager(person):
    def giveRaise(self,percent,bonus=.10):
        self.pay = int(self.pay * (1+percent+bonus))
        return self.pay
#类继承优化方法
class manager1(person):
    def giveRaise(self,percent,bonus=.10):
        person.giveRaise(self,percent + bonus)
        #一定要加return，否则随后的print test1.giveRaise(1)会产生None
        return self.pay

if __name__ == '__main__':
    bob = person('Bob Smith')
    sue = person('Sue',job='dev',pay=10000)
    print bob.name,bob.pay
    print sue.name,sue.job,sue.pay
    print bob.lastname()
    sue.giveRaise(.10)
    print sue.pay
    print sue
    test = manager('jake wolf',pay=10000)
    print test.giveRaise(1)
    #test1实例print 1（无需开启manage class的return）：
    test1 = manager1('jake wolf1',pay=10000)
    print test1.lastname()
    test1.giveRaise(1)
    print test1.pay
    #test1实例print 2（需要开启manage class的return）：
    test2 = manager('tom',pay=10000)
    #因为方法里直接return，所以直接使用方法print即可
    print test2.giveRaise(2)
