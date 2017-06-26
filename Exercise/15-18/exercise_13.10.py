#-*- coding: utf-8 -*-

class PerlArray(object):
    def __init__(self,li=[]):
        self.li = li
    def empty(self):
        if len(self.li) == 0:
            return 1
        else:
            return 0
    def shift(self):
        if self.empty():
            print '空数组'
        else:
            print 'remove [',self.li[0],']'
            self.li.remove(self.li[0])
    def unshift(self,value):
        print '在首位插入新值',value
        self.li.insert(0,value)
    def push(self,value):
        print '在队尾插入新值',value
        self.li.append(value)
    def pop(self):
        if self.empty():
            print '空数组'
        else:
            print 'remove: [',self.li.pop(),']'
    def listall(self):
        print self.li

if __name__ == '__main__':
    p = PerlArray([1,2,3,'q'])
    p.shift()
    p.listall()
    p.unshift(111)
    p.listall()
    p.push('qq')
    p.listall()
    p.pop()
    p.listall()