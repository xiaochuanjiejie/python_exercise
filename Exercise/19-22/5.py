#-*- coding: utf-8 -*-

class RoundFloat(object):
    def __init__(self,val):
        assert isinstance(val,float),'value must be a float'
        self.val = round(val,2)
    def __str__(self):
        return 'new float: %s' % self.val
    # __repr__ = __str__

p = RoundFloat(13.234)
# print p,'***'
# print dir(p)
# print p.val