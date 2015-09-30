#-*- coding: UTF-8 -*-
__author__ = 'chuan'
from lxml import etree
import requests
import re
import urllib2
import cookielib
import urllib
import cStringIO
# from pytesser import *
#避免 UnicodeEncodeError: 'ascii' codec can't encode character.  的报错
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

#下面这段是关键了，将为urlib2.urlopen绑定cookies
#MozillaCookieJar(也可以是 LWPCookieJar ，这里模拟火狐，所以用这个了) 提供可读写操作的cookie文件,存储cookie对象
cookiejar = cookielib.MozillaCookieJar()
# 将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
cookieSupport= urllib2.HTTPCookieProcessor(cookiejar)
#下面两行为了调试的
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的
opener = urllib2.build_opener(cookieSupport, httpsHandler)
#将包含了cookie、http处理器、http的handler的资源和urllib2对象绑定在一起，安装opener,此后调用urlopen()时都会使用安装过的opener对象，
urllib2.install_opener(opener)
content = urllib2.urlopen('http://www.zhihu.com#signin').read()
print content



# class zhihu_login():
#     def __init__(self):
#         self.url = 'http://www.zhihu.com'
#         self.url_login = 'http://www.zhihu.com/login/email'
#     def getsource(self):
#         html = requests.get(self.url_login).content
#         # print html
#         return html
#     def getdata(self,html):
#         selector = etree.HTML(html)
#         xsrf = selector.xpath('//div[@class="wrapper index-content-wrapper"]/div/div/div/div/div/form/input[@name="_xsrf"]/@value')[0]
#         # xsrf = selector.xpath('//input[@name="_xsrf"]/value')[0]
#         # xsrf = selector.xpath('//input[@name="_xsrf"]/@value')[0]
#         print xsrf
#         # auth_img = selector.xpath('//span/img[@height="30"]/@src')[0] //gif图随机生成，每次不一，暂缓
#         data = {
#             '_xsrf': xsrf,
#             'password': '821220',
#             'remember_me': 'true',
#             'email': 'xiaochuanjiejie@gmail.com'
#         }
# if __name__ == '__main__':
#     a = zhihu_login()
#     html = a.getsource()
#     a.getdata(html)
# s = requests.session()
# login_data = {'email':'xiaochuanjiejie@gmail.com','password':'821220',}
# s.post('http://www.zhihu.com/login',data=login_data)
# a = s.get('http://www.zhihu.com/people/FantasticCathy/answers').content
