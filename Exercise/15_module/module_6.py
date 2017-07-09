# coding: utf-8

def importAS(mymodule):
    newname = __import__(mymodule)
    return newname

if __name__ == '__main__':
    print importAS('sys')