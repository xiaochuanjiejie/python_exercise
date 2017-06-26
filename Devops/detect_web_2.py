# -*- coding: UTF-8 -*-
__author__ = 'chuan'

import pycurl
import time
import os,sys
sys.path.append('/Users/chuan/PycharmProjects/test/Devops')
from text_mail import send_mail

# URL1 = 'http://www.bjmcn.com/index.html'
# URL2 = 'http://eshop.bjmcn.com'

def URL(*args):
    print args
    for i in args:
        c = pycurl.Curl()
        c.setopt(pycurl.URL,i)
        c.setopt(pycurl.CONNECTTIMEOUT,5)
        c.setopt(pycurl.TIMEOUT,5)
        c.setopt(pycurl.NOPROGRESS,1)
        c.setopt(pycurl.FORBID_REUSE,1)
        c.setopt(pycurl.MAXREDIRS,1)
        c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)

        indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
        c.setopt(pycurl.WRITEHEADER,indexfile)
        c.setopt(pycurl.WRITEDATA,indexfile)

        #os.system('md5sum content.txt')
        #print '%s md5: %s' % (i,a)
        a = os.popen('md5sum content.txt').read().split()[0]
        print '%s md5: %s' % (i,a)

        try:
            c.perform()
        except Exception,e:
            print 'connection error: '+str(e)
            indexfile.close()
            c.close()
            sys.exit()

        HTTP_CODE = c.getinfo(c.HTTP_CODE)
        # print 'HTTP 状态码: %s' % HTTP_CODE
        if HTTP_CODE != 200:
            print 'Error(%s)' % HTTP_CODE

URL('http://www.bjmcn.com','http://eshop.bjmcn.com')

# if __name__ == '__main__':
#     URL()