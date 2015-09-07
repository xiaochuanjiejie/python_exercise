# -*- coding: UTF-8 -*-
__author__ = 'chuan'

import time
#初级装饰器
def log(func):
    def wrapper(*args,**kwargs):
        print 'call %s!' % func.__name__
        return func(*args,**kwargs)
    #若在此处wrapper函数后加()，则后续无需调用函数(即在写完代码不需加now())直接进行出结果了；若不加()，则后续需要写完装饰器后，加一行：now()
    #原理：加括号是函数调用，不加括号是个函数变量，相当于C的函数指针
    return wrapper
# ==: now = log(now)
#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
@log
def now():
    print 'current time is: %s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
now()
#此时因为以上代码执行的是now == log(now)，所以返回的now的__name__变为了：wrapper
print now.__name__

time.sleep(2)

#多层装饰器
def log2(text):
    def decorator(func2):
        def wrapper(*args,**kwargs):
            print '%s,%s' % (text,func2.__name__)
            return func2(*args,**kwargs)
        return wrapper()
    return decorator
# ==: now = log('excute')(now)
@log2('excute')
def now2():
    print 'current time is: %s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())