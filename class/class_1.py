# -*- coding: UTF-8 -*-
from

__author__ = 'chuan'

#from class_0 import firstclass     //两种方式均可
from


class secondclass(class_0.firstclass):
    def dispaly(self):
        print 'current value = "%s"' % self.data

z = secondclass()
z.setdata('bob')
z.dispaly()