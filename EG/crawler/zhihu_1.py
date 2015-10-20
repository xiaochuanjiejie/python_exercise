# -*- coding: UTF-8 -*-
__author__ = 'chuan'

from lxml import etree
import requests
import os
import time
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

# class zhihu():
#     def __init__(self):
#         self.url_login = 'http://www.zhihu.com/#signin'
#     def login(self):


class zhihu_login():
    def __init__(self):
        self.url = 'http://www.zhihu.com'
        self.url_login = 'http://www.zhihu.com/login/email'
    def getsource(self):
        html = requests.get(self.url_login).content
        print html
        return html
    # def getdata(self,html):
    #     selector = etree.HTML(html)
    #     xsrf = selector.xpath('//div[@class="wrapper index-content-wrapper"]/div/div/div/div/div/form/input[@name="_xsrf"]/@value')[0]
    #     # xsrf = selector.xpath('//input[@name="_xsrf"]/value')[0]
    #     # xsrf = selector.xpath('//input[@name="_xsrf"]/@value')[0]
    #     print xsrf
    #     # auth_img = selector.xpath('//span/img[@height="30"]/@src')[0] //gif图随机生成，每次不一，暂缓
    #     data = {
    #         '_xsrf': xsrf,
    #         'password': '821220',
    #         'captcha': ,
    #         'remember_me': 'true',
    #         'email': 'xiaochuanjiejie@gmail.com'
    #     }
if __name__ == '__main__':
    test = zhihu_login()
    test.getsource()
#     a = zhihu_login()
#     html = a.getsource()
#     a.getdata(html)
# s = requests.session()
# login_data = {'email':'xiaochuanjiejie@gmail.com','password':'821220',}
# s.post('http://www.zhihu.com/login',data=login_data)
# a = s.get('http://www.zhihu.com/people/FantasticCathy/answers').content