#-*- coding: utf-8 -*-

class Message(object):
    def __init__(self,msg='',broadcast=False,froms='',to=''):
        self.msg = msg
        self.broadcast = broadcast
        self.froms = froms
        self.to = to
    def __str__(self):
        if self.broadcast:
            return 'message: "%s" from %s send to everyone' % (self.msg,self.froms)
        else:
            return 'message: "%s" from %s send to %s' % (self.msg,self.froms,self.to)

class User(object):
    hear = {'everyone':''}
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    def talk(self,to='',msg=''):
        if to == 'everyone':
            m = Message(msg,True,self.name)
            User.hear['everyone'] = m
        elif to:
            m = Message(msg,False,self.name,to)
            User.hear[to] = m
        else:
            print 'receiver can not be empty'
    def hearmsg(self):
        if self.name in User.hear:
            print User.hear[self.name]
        elif User.hear['everyone']:
            print User.hear['everyone']
        else:
            print 'no message for %s' % self.name
    def talkroom(self,room,to='',msg=''):
        if to == 'everyone':
            m = Message(msg,True,self.name,to)
            room.receive(m)
        elif to:
            m = Message(msg,False,self.name,to)
            room.receive(m)
        else:
            print 'receiver can not be empty'
    def hearroom(self,m):
        print 'room %s' % m
    def createroom(self,name,count):
        return Room(name,count)

class Room(object):
    def __init__(self,rname,count=3):
        self.rname = rname
        self.count = count
        self.userlist = []
    def adduser(self,user):
        if len(self.userlist) <= self.count:
            self.userlist.append(user)
        else:
            print 'room user number limits'
    def receive(self,m):
        if m.broadcast:
            print 'room %s' % m
        else:
            for user in self.userlist:
                if user.name == m.to:
                    user.hearroom(m)


if __name__ == '__main__':
    test = Message('test message',True,'Jim','Cake')
    print test
    u1 = User('bob','male',33)
    u2 = User('jim','female',31)
    u3 = User('Tom','female',31)
    u1.talk(to='jim',msg='hi,jim')
    u2.hearmsg()
    u3.hearmsg()
    u1.talk(to='everyone',msg='hi,all...')
    u2.hearmsg()
    u3.hearmsg()
    room1 = u2.createroom('girls',2)
    room1.adduser(u2)
    room1.adduser(u3)
    u2.talkroom(room1,'Tom','hello,Tom')