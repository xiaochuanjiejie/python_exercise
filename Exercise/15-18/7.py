#-*- coding: utf-8 -*-

class Person(object):
    def __init__(self,age,name,height):
        t_dict = {'work':'it','salary':'10000'}
        self.age = age
        self.name = name
        self.height = height
        self.work = t_dict
    def what_name(self):
        print 'my name is' + self.name
    def how_old(self):
        print 'my age is %d' % self.age
    def how_height(self):
        print '{1}的身高是{0}米'.format(self.height,self.name)
    def print_work(self):
        for key in self.work:
            print key,':',self.work[key]

p = Person(18,"Tom",1.75)
p.what_name()
p.how_old()
p.how_height()
p.print_work()