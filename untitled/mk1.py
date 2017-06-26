#coding: utf-8

num = 10

class Foo(object):
    def test(self):
        print 'in mk1'

print 'mk1的 __name__: %s'  % __name__
if __name__ == '__main__':
    Foo().test()
Foo().test()    #若被别的模块调用，在import时会显示此行，若在__name__ == '__main__'里，则不会被调用