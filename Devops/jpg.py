# -*- coding: UTF-8 -*-
__author__ = 'chuan'

import urllib2,Image,urllib
url="http://image.artwow.net:8000/artwork/97C/000000000000497C_300x-.jpg"
req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
}
req_timeout = 5
req = urllib2.Request(url,None,req_header)
resp = urllib2.urlopen(req,None,req_timeout)
html = resp.read()
urllib.urlretrieve('http://image.artwow.net:8000/artwork/97C/000000000000497C_300x-.jpg',filename='2.jpeg')