#-*- coding: utf-8 -*-

class Stack(object):
    def __init__(self,t_list=[]):
        self.list = t_list
    def isempty(self):
        if len(self.list) == 0:
            return 1
        else:
            return 0
    def push(self,data):
        print '推入新数据: %s' % data
        self.list.append(data)
    def peek(self):
        if self.isempty():
            print '空栈'
        else:
            print self.list[-1:]
    def pop(self):
        if self.isempty():
            print '空栈'
        elif 'pop' in dir(self.list):
            print '内建pop方法移除数据: [',self.list.pop(),']'
        else:
            print '内建remove方法移除数据: [',self.peek(),']'
            self.list.remove(self.peek())
    def all(self):
        print self.list

if __name__ == '__main__':
    s1 = Stack()
    s1.peek()
    s2 = Stack([1,2,3,'a'])
    s2.all()
    s2.peek()
    s2.push(4)
    s2.all()
    s2.push('b')
    s2.all()
    s2.pop()