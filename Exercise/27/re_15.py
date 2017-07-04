#coding: utf-8

import re

card = raw_input('input card: ')
ss = re.search(r'(\d{4}-\d{4}-\d{4}-\d{4}|\d{4}-\d{6}-\d{5})',card)
print ss.group()