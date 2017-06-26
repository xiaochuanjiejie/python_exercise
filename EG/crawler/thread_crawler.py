# -*- coding: UTF-8 -*-
__author__ = 'chuan'
from multiprocessing.dummy import Pool as threadpool
import time
import requests

def getsource(link):
    html = requests.get(link)

urls = []
for i in range(1,21):
    url = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i)
    urls.append(url)

time1 = time.time()
for each in urls:
    print each
    getsource(each)
time2 = time.time()
print '单线程耗时： ' + str(time2-time1)

pool = threadpool(2)
time3 = time.time()
results = pool.map(getsource,urls)
pool.close()
pool.join()
time4 = time.time()
print '多线程耗时：' + str(time4-time3)
