__author__ = 'xujunchuan'
def foo(lst):
    d = locals()
    print type(d),d
    for key in d:
        if type(d[key]) is list:
            print key,type(key)
result = [1,2,3]
foo(result)

def foo(lst):
    d = globals()
    print type(d),type(lst),d
    for key in d:
        print d[key],'-----'
        if type(d[key]) is type(lst) and d[key] == lst:
            print key,type(key)
result1 = [1,2,3]
var = "hello"
foo(result1)
foo(var)

# def foo(arg, a):
#     x = 1
#     y = 'xxxxxx'
#     for i in range(10):
#         j = 1
#         k = i
#         print j,k
#     print locals()
# foo(1,2)