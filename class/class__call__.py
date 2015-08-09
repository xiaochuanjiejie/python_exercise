__author__ = 'chuan'

class test:
    def __init__(self,name):
        self.name = name
    def __call__(self):
        return '[My name is %s]' % self.name

s = test('xu')
print s()
