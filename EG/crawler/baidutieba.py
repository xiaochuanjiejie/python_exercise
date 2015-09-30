# -*- coding: UTF-8 -*-
__author__ = 'chuan'
from lxml import etree
from multiprocessing.dummy import Pool as threadpool
import requests,json,sys
reload(sys)
sys.setdefaultencoding('utf-8')

def spider(url):
    #抓取每个页面
    html = requests.get(url)
    selector = etree.HTML(html.text)
    #输出每个页面包含的所有'div[@class="l_post j_l_post l_post_bright  "]'元素
    content_field = selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    item = {}
    #循环每一个'div[@class="l_post j_l_post l_post_bright  "]'元素
    for each in content_field:
        # print each.xpath('@data-field')   //经过xpath处理后是一个仅包含一个元素的list，而后通过json将其处理为一个dict
        reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot',' '))
        # print reply_info
        author = reply_info['author']['user_name']
        reply_time = reply_info['content']['date']
        #对于图片为底板内嵌文字的内容是爬取不出来的
        content = each.xpath('div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')[0]
        print author
        print reply_time
        print content
        item['author'] = author
        item['reply_time'] = reply_time
        item['content'] = content
        write(item)
def write(value):
    # f = open('info.txt','a')
    f.writelines('回帖人：' + str(value['author']) + '\n')
    f.writelines('回帖时间：' + unicode(value['reply_time']) + '\n')
    f.writelines('回帖内容：' + value['content'] + '\n\n')
    # f.close()

if __name__ == '__main__':
    pool = threadpool(2)
    f = open('baidu_tieba.txt','a')
    page = []
    for i in range(1,21):
        loop_page = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i)
        page.append(loop_page)
    results = pool.map(spider,page)
    pool.close()
    pool.join()
    f.close()