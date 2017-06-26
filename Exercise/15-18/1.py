#-*- coding: utf-8 -*-

'''
python中的类 == 属性（数据） + 方法，比如做月饼的模子
面向对象有三个特性：封装、继承、多态
'''

class person(object):
    age = 18
    def study(self):
        print '18岁可以上大学了'
    def love(self):
        print '18岁可以谈恋爱了'

people = person()
print people.age
people.study()
people.love()