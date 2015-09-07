# -*- coding: UTF-8 -*-
__author__ = 'chuan'

# def get_no_of_instances(cls_obj):
#     return cls_obj.no_inst
# class Kls(object):
#     no_inst = 0
#     def __init__(self):
#         Kls.no_inst = Kls.no_inst + 1
#         print Kls.no_inst
# ik1 = Kls()
# ik2 = Kls()
# print(get_no_of_instances(Kls))

#coding: utf-8 #############################################################
# File Name: main.py
# Author: mylonly
# mail: [email]mylonly@gmail.com[/email]
# Created Time: Wed 11 Jun 2014 08:22:12 PM CST
#########################################################################
#!/usr/bin/python
import re,urllib2,HTMLParser,threading,Queue,time
#各图集入口链接
htmlDoorList = []
#包含图片的Hmtl链接
htmlUrlList = []
#图片Url链接Queue
imageUrlList = Queue.Queue(0)
#捕获图片数量
imageGetCount = 0
#已下载图片数量
imageDownloadCount = 0
#每个图集的起始地址，用于判断终止
nextHtmlUrl = ''
#本地保存路径
localSavePath = '/data/1920x1080/'
#如果你想下你需要的分辨率的，请修改replace_str,有如下分辨率可供选择1920x1200，1980x1920,1680x1050,1600x900,1440x900,1366x768,1280x1024,1024x768,1280x800
replace_str = '1920x1080'
replaced_str = '960x600'
#内页分析处理类
class ImageHtmlParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.nextUrl = ''
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        global imageUrlList
        if(tag == 'img' and len(attrs) > 2 ):
            if(attrs[0] == ('id','bigImg')):
                url = attrs[1][1]
                url = url.replace(replaced_str,replace_str)
                imageUrlList.put(url)
                global imageGetCount
                imageGetCount = imageGetCount + 1
                print url
        elif(tag == 'a' and len(attrs) == 4):
            if(attrs[0] == ('id','pageNext') and attrs[1] == ('class','next')):
            global nextHtmlUrl
            nextHtmlUrl = attrs[2][1];
  
#首页分析类
class IndexHtmlParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.urlList = []
        self.index = 0
        self.nextUrl = ''
        self.tagList = ['li','a']
        self.classList = ['photo-list-padding','pic']
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        if(tag == self.tagList[self.index]):
            for attr in attrs:
                if (attr[1] == self.classList[self.index]):
                    if(self.index == 0):
                    #第一层找到了
                    self.index = 1
                else:
                    #第二层找到了
                    self.index = 0
                    print attrs[1][1]
                    self.urlList.append(attrs[1][1])
                    break
            elif(tag == 'a'):
                for attr in attrs:
                    if (attr[0] == 'id' and attr[1] == 'pageNext'):
                        self.nextUrl = attrs[1][1]
                        print 'nextUrl:',self.nextUrl
                        break
  
#首页Hmtl解析器
indexParser = IndexHtmlParser()
#内页Html解析器
imageParser = ImageHtmlParser()
  
#根据首页得到所有入口链接
print '开始扫描首页...'
host = 'http://desk.zol.com.cn'
indexUrl = '/meinv/'
while (indexUrl != ''):
    print '正在抓取网页:',host+indexUrl
    request = urllib2.Request(host+indexUrl)
try:
    m = urllib2.urlopen(request)
    con = m.read()
    indexParser.feed(con)
    if (indexUrl == indexParser.nextUrl):
        break
    else:
        indexUrl = indexParser.nextUrl
except urllib2.URLError,e:
    print e.reason
    print '首页扫描完成，所有图集链接已获得：'
    htmlDoorList = indexParser.urlList
 
#根据入口链接得到所有图片的url
class getImageUrl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for door in htmlDoorList:
            print '开始获取图片地址,入口地址为:',door
            global nextHtmlUrl
            nextHtmlUrl = ''
            while(door != ''):
                print '开始从网页%s获取图片...'% (host+door)
                if(nextHtmlUrl != ''):
                    request = urllib2.Request(host+nextHtmlUrl)
                else:
                    request = urllib2.Request(host+door)
try:
    m = urllib2.urlopen(request)
    con = m.read()
    imageParser.feed(con)
    print '下一个页面地址为:',nextHtmlUrl
    if(door == nextHtmlUrl):
        break
    except urllib2.URLError,e:
        print e.reason
        print '所有图片地址均已获得:',imageUrlList
  
class getImage(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global imageUrlList
        print '开始下载图片...'
        while(True):
            print '目前捕获图片数量:',imageGetCount
            print '已下载图片数量:',imageDownloadCount
            image = imageUrlList.get()
            print '下载文件路径:',image
try:
    cont = urllib2.urlopen(image).read()
    patter = '[0-9]*\.jpg';
    match = re.search(patter,image);
    if match:
        print '正在下载文件：',match.group()
        filename = localSavePath+match.group()
        f = open(filename,'wb')
        f.write(cont)
        f.close()
        global imageDownloadCount
        imageDownloadCount = imageDownloadCount + 1
    else:
        print 'no match'
        if(imageUrlList.empty()):
            break
except urllib2.URLError,e:
    print e.reason
    print '文件全部下载完成...'
  
get = getImageUrl()
get.start()
print '获取图片链接线程启动:'
  
time.sleep(2)
  
download = getImage()
download.start()
print '下载图片链接线程启动:'