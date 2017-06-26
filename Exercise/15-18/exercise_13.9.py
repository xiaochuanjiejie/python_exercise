#-*- coding: utf-8 -*-

class Queue(object):
    def __init__(self,q=[]):
        self.queue = q
    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
    def enqueue(self,value):
        if self.empty():
            print '原始队列为空,插入指: %s' % value
            self.queue.append(value)
        else:
            self.queue.append(value)
    def dequeue(self):
        if self.empty():
            print '空队列'
        else:
            print 'remove [',self.queue[0],']'
            self.queue.remove(self.queue[0])
    def listall(self):
        print self.queue

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.listall()
    q.enqueue('qaz')
    q.listall()
    q.dequeue()
    q.listall()
