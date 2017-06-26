#coding: utf-8

mystr = 'i like python_global'

def foo():
    mystr = 'in foo_local...'
    print locals()

if __name__ == '__main__':
    foo()
    print globals()