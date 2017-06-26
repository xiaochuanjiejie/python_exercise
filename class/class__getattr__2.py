__author__ = 'chuan'

# class circle():
#     def __init__(self):
#         self.width=10
#         self.height=10
#     def __getattr__(self,name):
#         if name == 'size':
#             return [self.width,self.height]
#
# c=circle()
# print c.width
# print c.size1
# print c.size

class circle():
    def __init__(self):
        self.width=0
        self.height=0
    def __setattr__(self,name,value):
        if name == 'size':
            self.width=self.height=value
    def __getattr__(self,name):
        if name == 'size':
            return [self.width,self.height]

c=circle()
print c.size    #与上一段class相比，因为多了一个setattr方法，重载了__setattr__  所以 实例化的时候 __dict__ 被清空，你可以看下c.__dict__ 是空的, 然后你在insert 了一个size, __dict__ 里只有size 没有width和height