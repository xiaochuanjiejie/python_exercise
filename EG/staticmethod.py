__author__ = 'chuan'

class Person:
    def __init__(self):
        print 'init'
    @staticmethod
    def sayHello(hello):
        if not hello:
        # if hello:
        # if hello is not None:
        # if not hello is None:
            hello = '123'
        #     print hello
            print '###'
        print 'i will say %s' % hello
    # @classmethod
    def introduce(clazz,hello):
        clazz.sayHello(hello)
        print "from introduce method"
    def hello(self,hello):
        self.sayHello(hello)
        print "from hello method"

def main():
    Person.sayHello('hellow')
    # Person.introduce("hello world!")
    # p = Person()
    # p.sayHello('a')

if __name__ == '__main__':
    main()