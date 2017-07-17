#coding: utf-8
'''
10-1.引发异常。以下的哪个因素会在程序执行时引发异常？注意这里我们问的并不是异常的原因。
答：用户和程序

10-2.引发异常。参考上边问题的列表，哪些因素会在执行交互解释器时引发异常？ 答案：f（用户和程序）
10-3.关键字。用来引发异常的关键字有哪些？ 答案：raise 
10-4.关键字。try-except和try-finally有什么不同？ 
    答：  
    try-except：当try代码块运行出错，except代码块才会被执行（匹配到相应异常时），处理完异常后try-except后的代码会继续往下执行；  
    try-finally：不管try代码块是否出现异常，最终都会执行finally里的代码。如果出现异常，执行完finally代码块后，异常会继续往上层抛。
10-5.异常。下面这些交互解释器下的Python代码段分别会引发什么异常
(a) >>>if 3 < 4 then:print '3 is less than 4!' 
    异常：SyntaxError: invalid syntax
(b) >>>aList = ['Hello','World','Anyone','Home?']
    >>>print 'the last string in aList is: ',aList[len(aList)]
    异常：IndexError: list index out of range
(c) >>>x
    异常：NameError: name 'x' is not defined
(d) >>>x = 4 % 0
    异常：ZeroDivisionError: integer division or modulo by zero
(e) >>>import math
    >>>i = math.sqrt(-1)
    异常：ValueError: math domain error
'''