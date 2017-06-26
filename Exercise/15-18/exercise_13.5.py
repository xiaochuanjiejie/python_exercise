#-*- coding: utf-8 -*-

class point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return 'x_value is %d,y_value is %d' % (self.x,self.y)

if __name__ == '__main__':
    p = point(1,2)
    print p