#-*- coding: UTF-8 -*-
__author__ = 'chuan'

from lxml import etree
from email.mime.text import MIMEText
import smtplib
import requests
import os
import time
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

class send_mail():
    def __init__(self):
        self.mail_host = 'smtp.sina.com'
        self.mail_user = 'onelamp2001'
        self.mail_pass = '821221'
        self.mail_postfix = 'sina.com'
    def send(self,to_list,sub,content):
        me="xxoohelper"+"<"+self.mail_user+"@"+self.mail_postfix+">"
        msg = MIMEText(content,_subtype='plain',_charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user,self.mail_pass)
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            return True
        except Exception, e:
            print str(e)
            return False
class xxoo():
    def __init__(self):
        self.url = 'http://weibo.cn/u/3482557617'
        self.url_login = 'http://login.weibo.cn/login/'
        # self.new_url = self.url_login
    def getsource(self):
        html = requests.get(self.url).content
        return html
    def getdata(self,html):
        selector = etree.HTML(html)
        password = selector.xpath('//input[@type="password"]/@name')[0]
        vk = selector.xpath('//input[@name="vk"]/@value')[0]
        # action = selector.xpath('//form/@action')[0]与下一行同理
        action = selector.xpath('//form[@method="post"]/@action')[0]
        self.new_url = self.url_login + action
        data = {
            'mobile': 'xiaochuanjiejie@gmail.com',
            password: '821220jie',
            'remember': 'on',
            'backURL': 'http://weibo.cn/u/3482557617',
            'backTitle': u'微博',
            'tryCount': '',
            'vk': vk,
            'submit': u'登录'
        }
        return data
    def getcontent(self,data):
        newhtml = requests.post(self.new_url,data=data).content
        new_selector = etree.HTML(newhtml)
        content = new_selector.xpath('//span[@class="ctt"]')
        newcontent = unicode(content[2].xpath('string(.)'))
        print newcontent
        newcontent_time = new_selector.xpath('//span[@class="ct"]/text()')[0]
        sendtext =newcontent + newcontent_time
        return sendtext
    def write(self,text):
        f = open('weibo.txt','a')
        f.write(text + '\n')
        f.close()
    def tocheck(self,data):
        if not os.path.exists('weibo.txt'):
            return True
        else:
            f = open('weibo.txt','r')
            existweibo = f.readlines()
            if data + '\n' in existweibo:
                return False
            else:
                return True

if __name__ == '__main__':
    mail_list = ['33734898@qq.com']
    weibohelp = xxoo()
    while True:
        source = weibohelp.getsource()
        data = weibohelp.getdata(source)
        content = weibohelp.getcontent(data)
        if weibohelp.tocheck(content):
            if send_mail().send(mail_list,u'微博更新了',content):
                print u'send sucess'
            else:
                print u'send failed'
            weibohelp.write(content)
        else:
            print u'pass'
        time.sleep(15)