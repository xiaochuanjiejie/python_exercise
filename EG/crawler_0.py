# -*- coding: UTF-8 -*-
__author__ = 'chuan'

import requests
import re
import sys
head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'}
html = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=python&fr=search',headers = head)
# print html.text

text = re.findall('<link rel="stylesheet" href="(.*?)" />',html.text,re.S)
for each in text:
    print each
