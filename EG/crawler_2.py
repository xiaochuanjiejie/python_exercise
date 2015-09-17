# -*- coding: UTF-8 -*-
__author__ = 'chuan'
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class spider():
    #构造函数
    def __init__(self):
        print '开始爬取内容...'
    #爬取每个页面的源代码
    def getsource(self,urllink):
        head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'}
        html = requests.get(urllink,headers = head)
        return html.text
    #爬取页面内每个学习模块
    def geteveryclass(self,sour):
        everyclass = re.findall('<li id="(.*?)</li>',sour,re.S)
        # everyclass = re.findall('<li deg="".*?</li>',sour,re.S)
        return everyclass
    #爬取每个学习模块的具体信息
    def getinfo(self,eachclass):
        info = {}
        info['title'] = re.search('title="(.*?)">',eachclass,re.S).group(1)
        info['content'] = re.search('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>',eachclass,re.S).group(1)
        timeandlevel = re.findall('<em>(.*?)</em>',eachclass,re.S)
        info['time'] = timeandlevel[0]
        info['level'] = timeandlevel[1]
        #就是此处，下面两行有歧义（表达意思都一样，但一个可以执行一个不能执行）：因为要去掉style="display: none;查看页面实际源代码是没有此项，仅通过开发者工具是有的
        info['learnnum'] = re.search('"learn-number">(.*?)</em>',eachclass,re.S).group(1)
        # info['learnnum'] = re.search('<em class="learn-number" style="display: none;">(.*?)</em>',eachclass,re.S).group(1)
        return info
    #产生不同页数的链接
    def changepage(self,url,total_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []
        for i in range(now_page,total_page+1):
            link = re.sub('pageNum=(\d+)','pageNum=%s' % i,url,re.S)
            page_group.append(link)
        return page_group
    #将采集信息写入info.txt
    def saveinfo(self,classinfo):
        f = open('info.txt','w')
        for eachclassinfo in classinfo:
            f.writelines('title:' + eachclassinfo['title'] + '\n')
            f.writelines('content:' + eachclassinfo['content'] + '\n')
            f.writelines('time:' + eachclassinfo['time'] + '\n')
            f.writelines('level:' + eachclassinfo['level'] + '\n')
            f.writelines('learnnum:' + eachclassinfo['learnnum'] + '\n\n')
        f.close()
if __name__ == '__main__':
    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider = spider()
    all_links = jikespider.changepage(url,2)
    for link in all_links:
        print '处理页面中...' + link
        html = jikespider.getsource(link)
        everyclass = jikespider.geteveryclass(html)
        for each in everyclass:
            info = jikespider.getinfo(each)
            classinfo.append(info)
    # print classinfo
    jikespider.saveinfo(classinfo)
