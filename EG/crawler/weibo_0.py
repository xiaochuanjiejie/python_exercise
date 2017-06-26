#-*- coding: UTF-8 -*-
__author__ = 'chuan'

from lxml import etree
import requests
#有些页面的编码保存出来时会出现编码错误，使用以下三行代码，将编码强制转换为UTF-8
#避免 UnicodeEncodeError: 'ascii' codec can't encode character.  的报错
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://weibo.cn/u/3482557617'
url_login = 'http://login.weibo.cn/login/'
html = requests.get(url).content
selector = etree.HTML(html)
#输出eg: ['password_9310']
# password = selector.xpath('//input[@type="password"]/@name')
#输出eg: password_9130
password = selector.xpath('//input[@type="password"]/@name')[0]
vk = selector.xpath('//input[@name="vk"]/@value')[0]
# action = selector.xpath('//form/@action')[0]与下一行同理
action = selector.xpath('//form[@method="post"]/@action')[0]
print password
print vk
print action

new_url = url_login + action
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

html2 = requests.post(new_url,data=data).content
new_selector = etree.HTML(html2)
content = new_selector.xpath('//div/span[@class="ctt"]')
for i in content:
    #使用string(.)将<span class="ctt">---</span>标签下的文本都显示出来
    text = i.xpath('string(.)')
    # b = 1
    print text