#-*- coding: utf-8 -*-

from datetime import datetime
import shelve,os

class userdatabase(object):
    def __init__(self,dbfile):
        # self.db = {}
        # if os.path.exists(dbfile):
        self.db = shelve.open(dbfile,'c')
        self.dbfile = dbfile
        self.flag = False
    def login(self,user,pwd):
        if not self.db.has_key(user):
            self.flag = False
            print '%s first login' % user
            self.db[user] = [pwd,datetime.now()]
            print self.db[user]
        elif self.db[user][0] == pwd:
            self.db[user][1] = datetime.now()
            self.flag = True
            print 'login success'
    def deluser(self,user):
        if self.flag:
            self.db.pop(user)
        else:
            print 'first login'
    def update(self,user,pwd):
        if self.flag:
            self.db[user] = [pwd,datetime.now()]
        else:
            print 'first login'
    def listall(self):
        if self.flag:
            for user in self.db:
                print user,self.db[user][0],self.db[user][1]
        else:
            print 'first login'

if __name__ == '__main__':
    test = userdatabase('/tmp/shelve.data')
    test.login('t1','123')
    test.listall()
    test.update('t1','qweasd')
    test.listall()