# -*- coding: UTF-8 -*-
__author__ = 'chuan'

import xlrd
import time
import smtplib
# from email.MIMEText import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

localtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# f = open('%s.txt' % localtime,'w')
# print >> f,'123'
# f.close()
input_data_1 = raw_input('Please input source_file_name: ')
input_data_2 = raw_input('Please input total_file_name: ')

def open_excel_1():
    try:
        file1 = xlrd.open_workbook(filename='/Users/chuan/Documents/%s' % input_data_1)
        return file1
    except Exception,e:
        print 'error is :'+str(e)
def open_excel_2():
    try:
        file2 = xlrd.open_workbook(filename='/Users/chuan/Documents/%s' % input_data_2)
        return file2
    except Exception,e:
        print 'error is :'+str(e)
def excel_table_byindex():
    data1 = open_excel_1()
    table1 = data1.sheets()[0]
    nrows1 = table1.nrows
    ncols1 = table1.ncols
    data2 = open_excel_2()
    table2 = data2.sheets()[0]
    nrows2 = table2.nrows
    ncols2 = table2.ncols
    # print '总行数: %s;总列数: %s' % (nrows,ncols)
    list1,list2,list3,list_res_1,list_res_2 = [],[],[],[],[]
    colname = input('请输入选择列数，用阿拉伯数字代表(0代表第一列，以此类推): ')
    for q in range(nrows2):
        b = table2.col_values(colname)
        list2.append(b)
        num2 = '%d' % list2[0][q]
        list3.append(num2)
    for i in range(nrows1):
        #输出第一列值
        a = table1.col_values(colname)
        list1.append(a)
        num = '%d' % list1[0][i]
        if num in list3:
            list_res_1.append(num)
            # f = open('out1.txt','w')
            # print >> f,'%s在总表内，NO_extract' % num
            # f.close()
        else:
            list_res_2.append(num)
            # print '%s不在总表内，需要处理' % num
    # print list_res_1[0],list_res_2
    f = open('%s NO_extract.txt' % localtime,'w')
    print >> f,'%s NO_extract' % list_res_1
    f.close()
    h = open('%s YES_extract.txt' % localtime,'w')
    print >> h,'%s 需要处理(YES_extract)' % list_res_2
    h.close()

    #测试
    # print table.row(0)[0].value
    # print table.row_values(0)
    # a = table.col_values(0)
    # list.append(a)
    # print list[0][2]

if __name__ == '__main__':
    excel_table_byindex()
    HOST = 'smtp.qq.com'
    SUBJECT = u'新增ID处理'
    TO = '110831402@qq.com'
    FROM = '33734898@qq.com'

    msg = MIMEMultipart('related')
    attach = MIMEText(open('%s YES_extract.txt' % localtime,'rb').read(),"base64","utf-8")
    attach["Content-Type"] = "application/octet-stream"
    attach["Content-Disposition"] = "attachment;filename=\"需要处理的ID.txt\"".decode("utf-8").encode("gb18030")

    msg.attach(attach)
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = TO
    try:
        server = smtplib.SMTP()
        server.connect(HOST,'25')
        server.starttls()
        server.login('33734898','821220jieqaz')
        server.sendmail(FROM,TO,msg.as_string())
        server.quit()
        print 'send mail access'
    except Exception,e:
        print 'send mail failed: '+str(e)

# file = xlrd.open_workbook(filename='/Users/chuan/Documents/%s' % input_data)
# print file
# 使用QQ邮箱发送报错：
# 454 Authentication failed, please open smtp flag first!
# 在QQ邮箱的设置里面，设置-》账户-》POP3/IMAP/SMTP选择开启POP3/SMTP服务