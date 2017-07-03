#coding: utf-8

import re

address = '1019 De la Cruz Bouelvard 2089 Bordeaux Drive 12312738123'
ss = re.search(r'[\d]+\s[a-zA-Z\s]+',address)
# ss = re.search(r'[\d]+\ [a-zA-Z\ ]+',address)
print ss.group()

ss1 = re.findall(r'[\d]+\s[a-zA-Z\s]+',address)
print ss1