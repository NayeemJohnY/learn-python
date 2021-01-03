Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sq=[1,4,5,6,8]
>>> sq[4]
8
>>> sq[5]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    sq[5]
IndexError: list index out of range
>>> sq[-5]
1
>>> sq[:]
[1, 4, 5, 6, 8]
>>> sq[:5]
[1, 4, 5, 6, 8]
>>> sq[5:]
[]
>>> sq[2:5]
[5, 6, 8]
>>> sq+[10,15,50]
[1, 4, 5, 6, 8, 10, 15, 50]
>>> sq+[-1]
[1, 4, 5, 6, 8, -1]
>>> sq+_
[1, 4, 5, 6, 8, 1, 4, 5, 6, 8, -1]
>>> sq=sq-_
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    sq=sq-_
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> sq
[1, 4, 5, 6, 8]
>>> sq+sq_
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    sq+sq_
NameError: name 'sq_' is not defined
>>> sq=sq+_
>>> sq
[1, 4, 5, 6, 8, 1, 4, 5, 6, 8]
>>> sq=_-sq
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    sq=_-sq
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> sq
[1, 4, 5, 6, 8, 1, 4, 5, 6, 8]
>>> sq=sq-_
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    sq=sq-_
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> sq
[1, 4, 5, 6, 8, 1, 4, 5, 6, 8]
>>> sq[3]=18
>>> sq
[1, 4, 5, 18, 8, 1, 4, 5, 6, 8]












