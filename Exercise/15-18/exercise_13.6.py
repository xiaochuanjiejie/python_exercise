#-*- coding: utf-8 -*-

from math import sqrt

class Line(object):
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.length = 0
        self.slope = 0
    def getlength(self):
        if (self.x1 == self.x2) and (self.y1 == self.y2):
            self.length = 0
        elif self.x1 == self.x2:
            self.length = abs(self.y2 - self.y1)
        elif (self.y1 == self.y2):
            self.length = abs(self.x2 - self.x1)
        else:
            self.length = sqrt(abs(self.x2 - self.x1) ** 2 + abs(self.y2 - self.y1) ** 2)
        return self.length
    def getslope(self):
        if self.length == 0:
            self.slope = None
        elif (self.x1 == self.x2) or (self.y1 == self.y2):
            self.slope = None
        else:
            self.slope = (self.y2 - self.y1) / (self.x2 - self.x1)
        return self.slope
    def __str__(self):
        return '坐标属性：((%d,%d),(%d,%d))' % (self.x1,self.y1,self.x2,self.y2)
    def __repr__(self):
        return '((%d,%d),(%d,%d))' % (self.x1,self.y2,self.x2,self.y2)

l = Line(1,2,3,4)
print l
print '%r' % l
print l.getlength()
print l.getslope()