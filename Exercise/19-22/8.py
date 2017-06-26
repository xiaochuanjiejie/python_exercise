>>> x = 'abc'
>>> x1 = 'abc'
>>> x2 = repr(x1)
>>> x1
'abc'
>>> x2
"'abc'"
>>> eval(x2)
'abc'
>>> print type(x2)
<type 'str'>
>>> print type(x1)
<type 'str'>
>>> x3 = str(x1)
>>> eval(x3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1, in <module>
NameError: name 'abc' is not defined
>>>