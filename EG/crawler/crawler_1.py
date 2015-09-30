# -*- coding: UTF-8 -*-
__author__ = 'chuan'

import requests
import re
import sys
head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'}
html = requests.get('https://www.crowdfunder.com/deals',headers = head)
# print html

text = re.findall('<a href="/(.*?)/invest" class="card-link">View Company</a>',html.text,re.S)
for each in text:
    print each