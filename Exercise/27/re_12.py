#coding: utf-8

import re

domain = raw_input('input domain: ')
ss = re.search(r'www\.[\w-]+\.(com|net|edu|com.cn)$',domain)
