#coding: utf-8

import re

ss = re.search('b.*t|h.*t','bat bit but hat hit hut sgt asjc 123sa')
print ss.group()