__author__ = 'chuan'

import threading

local_school = threading.local()

def process_student():
    print 'Hello,%s in %s' % (local_school.name,threading.currentThread().name)

def process_school(student_name):
    local_school.name = student_name
    process_student()

t1 = threading.Thread(target=process_school,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_school,args=('Jack',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
