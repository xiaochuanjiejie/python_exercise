#coding: utf-8

def new_open(filename,mode='r'):
    try:
        f = open(filename,mode)
    except IOError:
        return None
    return f

if __name__ == '__main__':
    f1 = new_open('error_1.py')
    print f1