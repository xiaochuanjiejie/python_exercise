__author__ = 'chuan'

import requests
from lxml import etree

url = 'http://weibo.cn/ci123456'
cook = {"Cookie":"_T_WM=c2b254ddc828372b07853fbbf4b9ba35; SUB=_2A254_8jdDeTxGedJ7loX8y3PyTuIHXVYA-iVrDV6PUJbrdANLW2hkW0lwaBjMs7A49TsDlhgF0IoKaw2Tg..; gsid_CTandWM=4uNG1631169VGM23Rxs397nv35h"}
html = requests.get(url,cookies = cook)
print html.text
