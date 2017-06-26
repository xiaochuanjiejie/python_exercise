#-*- coding: utf-8 -*-

import time

class TimeFMT(object):
    def __init__(self,t=time.time()):
        self.time = t
    def update(self,t=time.time()):
        self.time = t
    def display(self,usert=None):
        time_format = {}
        time_format['MDY'] = '%m/%d/%y'
        time_format['MDYY'] = '%m/%d/%Y'
        time_format['DMY'] = '%d/%m/%y'
        time_format['DMYY'] = '%d/%m/%Y'
        time_format['MODYY'] = '%b %d,%Y'
        if usert in time_format:
            midt = time.localtime(self.time)
            print time.strftime(time_format[usert],midt)
        else:
            print '默认使用ctime方法: %s' % time.ctime(self.time)

if __name__ == '__main__':
    t = TimeFMT()
    t.display()
    t.display('MDYY')
    t.update(time.time()+600)
    t.display()