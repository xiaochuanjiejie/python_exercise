# -*- coding: UTF-8 -*-
__author__ = 'chuan'

import smtplib
import string

def send_mail(*args):
    l = list(args)
    HOST = 'smtp.qq.com'
    SUBJECT = 'Web monitor'
    TO = 'xiaochuanjiejie@163.com'
    FROM = '33734898@qq.com'
    text = 'web status is: %s;%s MD5 is %s,warning!' % (l[0],l[1],l[2])
    BODY = string.join((
            "From: %s" % FROM,
            "To: %s" % TO,
            "Subject: %s" % SUBJECT,
            "",
            text
            ),"\r\n")
    server = smtplib.SMTP()
    server.connect(HOST,'25')
    server.starttls()
    server.login('33734898','821220jieqaz')
    server.sendmail(FROM,TO,BODY)
    server.quit()
send_mail(HTTP_CODE,i,a)

