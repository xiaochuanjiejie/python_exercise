# -*- coding: UTF-8 -*-
#windows下的多进程编写，因为windows没有fork()调用
__author__ = 'chuan'

from multiprocessing import Process
import os

def run_proc(name):
    print 'Run child process %s (%s)...' % (name,os.getpid())

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    #两种p的实例创建方法，只有第一种才是正确方法
    p = Process(target=run_proc,args=('test',))
    # p = Process(target=run_proc('test'))
    print 'Child process will start'
    p.start()
    p.join()
    print 'Child process end.'
