#-*- coding: utf-8 -*-

class Time60(object):
    '''
    三种输入:(10,30),({'hr':10,'min':30}),("10:30")。初始化函数分为两种判断，字符串和非字符串匹配
    '''
    def __init__(self,hr=0,min=0):
        if isinstance(hr,str):
            tmp = hr.split(':')
            self.hr = int(tmp[0])
            self.min = int(tmp[1])
        else:
            self.hr = hr
            self.min = min
    def __str__(self):
        return '%02d:%02d' % (self.hr,self.min)
    def __repr__(self):
        return repr('%02d:%02d' % (self.hr,self.min))
    def __add__(self, other):
        hr = self.hr + other.hr
        min = self.min + other.min
        thr = hr // 60
        # min = min % 60
        if min > 60:
            thr += 1
            min = min % 60
            hr += thr
        elif min == 60:
            thr += 1
            min = 0
            hr += thr
        else:
            min % 60
            hr += thr
        return self.__class__(hr,min)
    def __iadd__(self, other):
        # self.hr += other.hr
        # self.min += other.min
        return self.__add__(other)

if __name__ == '__main__':
    print Time60()
    print Time60(12,5)
    print Time60(*(22,5))
    print Time60(**{'hr':8,'min':9})
    print Time60('7:12')
    print Time60('8:30') + Time60('9:50')
    print Time60('10:30') + Time60('8:45')
    m1 = Time60(10,30)
    m2 = Time60(8,45)
    print m1
    print id(m1)
    m1 += m2
    print id(m1)
    print m1