#-*- coding: utf-8 -*-

#书例
class SortedKeyDict(dict):
    def keys(self):
        return sorted(super(SortedKeyDict,self).keys())

d = SortedKeyDict((('zheng-cai',1),('hui-jun',2),('xin-yi',3),('ya-i',4)))
print 'By iterator:'.ljust(20),[keys for keys in d]
print 'By keys():'.ljust(20),d.keys()
if isinstance(d,SortedKeyDict):
    print '11'
#习题
class SortedKeyDict_2(dict):
    def keys(self):
        # return sorted(dict.keys())
        return sorted(super(SortedKeyDict_2,self).keys())
d2 = SortedKeyDict_2((('zheng-cai',1),('hui-jun',2),('xin-yi',3),('ya-i',4)))
# 会产生错误，无穷递归。因为self.keys()又会调用自身的方法keys()
print d2.keys()
# 规避方法:不会做