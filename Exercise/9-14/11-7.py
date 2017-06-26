__author__ = 'xujunchuan'

def connect(list1,list2):
    if len(list1) != len(list2):
        print 'can not connect list'
    else:
        print map(None,list1,list2)
        print zip(list1,list2)

connect([1,2,3],['a','b','c'])