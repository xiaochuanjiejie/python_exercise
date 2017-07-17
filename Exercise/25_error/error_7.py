#coding: utf-8

'''
异常。下面两端Python伪代码a)和b)有什么区别？考虑语句A和B的上下文环境。
 (a)  
 try:          
    statement_A      
 except:
    ...
 else:         
    statement_B    
 (b)  
 try:          
    statement_A         
    statement_B      
 except:
    ...
    
答：
1.  若statement_A异常，statement_B在a和b中都不会被执行；
2.  若statement_A正常，statement_B在a和b中都会被执行。而后，若statement_B异常，在b中会被except捕获，在a中只能将statement_B的异常抛给上层调用者。
'''