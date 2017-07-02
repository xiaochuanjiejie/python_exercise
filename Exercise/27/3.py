#coding: utf-8

with open('temp.txt') as f:
    # for line in f.readlines():      #把文件全读取到内存中，然后逐行print
    #     print line,
    # while True:
    #     for line in f.readline():       #只读了一行，若想一直往下读，需要写到while true里
    #         print line,
    # for line in f.read():
    #     print line
    # print f.read(1)     #按照给定的字节数进行读取，读取出来后是个str
    while True:
        a = f.readline()
        print a
        if not a: break
print '---'
# with open('temp.txt') as f:
#     print f.read(3)
# f1 = open('temp.txt','r')
# for line in open('temp.txt'):
#     line = f1.readline()
#     print line
# f.close()