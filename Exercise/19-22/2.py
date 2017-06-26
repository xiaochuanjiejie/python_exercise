#-*- coding: utf-8 -*-

class P1:

    def foo(self):
        print 'called p1'

class P2:

    def foo(self):
        print 'called p2-foo'

    def bar2(self):
        print 'called p2-bar2'


class C1(P1,P2):

    pass

class C2(P1,P2):

    def bar2(self):
        print 'called c2-bar'

class Gc(C1,C2):

    pass

gc = Gc()
gc.foo()
gc.bar2()