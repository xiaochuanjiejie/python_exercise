# -*- coding: UTF-8 -*-
__author__ = 'Administrator'

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
class manage(person):
    def __init__(self,name,pay):
        person.__init__(self,name,'mgr',pay)
    def giveRaise(self,percent,bonus=.10):
        person.giveRaise(self,percent + bonus)

if __name__ == '__main__':
    sue = manage('tom link',50000)
    sue.giveRaise(.10)
    print sue
