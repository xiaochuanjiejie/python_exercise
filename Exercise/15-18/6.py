#-*- coding: utf-8 -*-

class Foo(object):
    """如果类属性是不可变的，通过实例无法修改；如果类属性是可变的（eg: list），通过实例可以修改"""
    x = 1
    t_list = [1]

print 'x初始值: %d' % Foo.x
Foo.x += 1
print '类Foo.x初始值变为: %d' % Foo.x

p = Foo()
print p.__doc__
print '实例p的x初始值为: %d' % p.x
p.x += 1
print '实例p的x变为: %d' % p.x
print '类Foo.x值仍为: %d，实例对x属性的改造并未影响到类Foo' % Foo.x

print '类Foo.list初始值为: %s，实例p.list初始值为: %s' % (Foo.t_list,p.t_list)
p.t_list.append(222)
print '类Foo.list值为: %s，实例p.list值变为: %s' % (Foo.t_list,p.t_list)


