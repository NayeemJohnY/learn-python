Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word="python"
>>> word[-6]
'p'
>>> word[0:5]
'pytho'
>>> word[:3]
'pyt'
>>> word[:2]
'py'
>>> word[:3]+word[3:]
'python'
>>> word[:2]+word[3:]
'pyhon'
>>> word[4:42]
'on'
>>> word[42:]
''
>>> word[42:]+word[:42]
'python'
>>> word[0]="C"
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    word[0]="C"
TypeError: 'str' object does not support item assignment
>>> word[0]='D'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    word[0]='D'
TypeError: 'str' object does not support item assignment
>>> len(word)
6
>>> 
