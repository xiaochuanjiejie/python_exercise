__author__ = 'chuan'

import difflib

text1 = '''text1:
compare(a, b)

      Compare two sequences of lines, and generate the delta (a
      sequence of lines).

      Each sequence must contain individual333 single-line strings ending
      with newlines.  Such sequences can be obtained from the
      "readlines()" method of file-like objects.  The delta generated
      also consists of newline-terminated strings, ready to be printed
      as-is via the "writelines()" method of a file-like object.
'''
text1_line =text1.splitlines()

text2 = '''text2:
compare(a, b)

      Compare two sequences of lines, and generate the delta (a
      sequence of lines).

      Each sequence must contain individual single-line strings1111 ending
      with newlines.  Such sequences can be obtained from the
      "readlines()" method of file-like objects.  The delta generated
      also consists of newline-terminated strings, ready to be printed
      as-is via the "writelines()" method of a file-like object22222.
'''
text2_line = text2.splitlines()

d = difflib.HtmlDiff()
print d.make_file(text1_line,text2_line)