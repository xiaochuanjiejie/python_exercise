
class t(object):

    def __init__(self,farg=1,**kwargs):
        self.farg = farg
        for item in kwargs:
            print item,kwargs[item]

class t2(object):
    def __init__(self,hr=0,min=0):
        self.hr = hr
        self.min = min
    def __str__(self):
        return '%02d:%02d' % (self.hr,self.min)

if __name__ == '__main__':
    d = {'a':1,'b':2}
    test1 = t(333,**d)
    test1

    test2 = t2(**{'hr':2,'min':45})
    print test2
    test3 = t2(*(3,23))
    print test3