# -*- coding: UTF-8 -*-
__author__ = 'chuan'

def send_mail(*args):
    print args
    print '...'
    for toMail in args:
        print toMail
        import smtplib
        from email.MIMEText import MIMEText
        from email.Utils import formatdate
        from email.Header import Header
        import sys

        smtpHost = 'smtp.mxhichina.com'
        smtpPort = '25'
        sslPort  = '465'
        fromMail = 'postmaster@intern-mate.com'
        toMail   = toMail
        username = 'postmaster@intern-mate.com'
        password = 'Sxgs2015'

        reload(sys)
        sys.setdefaultencoding('utf8')

        subject  = u'实习工社'
        body     = u'测试'

        encoding = 'utf-8'
        mail = MIMEText(body.encode(encoding),'plain',encoding)
        mail['Subject'] = Header(subject,encoding)
        mail['From'] = fromMail
        mail['To'] = toMail
        mail['Date'] = formatdate()

        try:
            smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
            smtp.ehlo()
            smtp.login(username,password)

            smtp.sendmail(fromMail,toMail,mail.as_string())
            smtp.close()
            print 'OK'
        except Exception:
            print 'Error: unable to send email'

send_mail('xiaochuanjiejie@163.com','33734898@qq.com','onelamp2001@sina.com','sldlx@sohu.com','xiaochuanjiejie@gmail.com','shixigongshe123@126.com')