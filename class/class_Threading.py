__author__ = 'chuan'

import time,threading

def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name,n)
        time.sleep(2)
    print 'thread %s is ended' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop,name='LoopThread1')
t.start()
t.join()
print 'thread %s is ended...' % threading.currentThread().name
