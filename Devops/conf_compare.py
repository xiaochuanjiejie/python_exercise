__author__ = 'chuan'

import difflib
import sys

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception,e:
    print 'Error:'+str(e)
    print 'Usage: conf_compare.py nginx.conf.1 nginx.conf.2'
    sys.exit()
def readline(filename):
    try:
        file = open(filename,'rb')
        text = file.read().splitlines()
        file.close()
        return text
    except IOError as error:
        print 'Read file Error:'+str(error)
        sys.exit()

text_file1 = readline(textfile1)
text_file2 = readline(textfile2)

diff = difflib.HtmlDiff()
print diff.make_file(text_file1,text_file2)