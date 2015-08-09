__author__ = 'chuan'

class myobject:
    def __len__(self):
        return 100

a = myobject()
print  len(a)
print  'abc'.__len__()
print len('abc')