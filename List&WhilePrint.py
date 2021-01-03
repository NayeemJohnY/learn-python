Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=["Nayyem", "John" "SDET"]
>>> b=[3,4,9]
>>> x=[a b]
SyntaxError: invalid syntax
>>> 
>>> 
>>> x=[a,b]
>>> x
[['Nayyem', 'JohnSDET'], [3, 4, 9]]
>>> x
[['Nayyem', 'JohnSDET'], [3, 4, 9]]
>>> x[0][1]
'JohnSDET'
>>> x[0][1]=_-"SDET"
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x[0][1]=_-"SDET"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> x[0][1]="John"
>>> x
[['Nayyem', 'John'], [3, 4, 9]]
>>> x[0][0]="Nayeem"
>>> x
[['Nayeem', 'John'], [3, 4, 9]]
>>> x[0][2]="SDET"
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x[0][2]="SDET"
IndexError: list assignment index out of range
>>> x.append("DS")
>>> x
[['Nayeem', 'John'], [3, 4, 9], 'DS']
>>> x[0].append("SDET")
>>> x
[['Nayeem', 'John', 'SDET'], [3, 4, 9], 'DS']
>>> 
>>> 

>>> 

>>> 




>>> 
>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> a, b=0,1
>>> a
0
>>> b
1
>>> while a<10:
	print(a)
	a,b=b,a+b

	
0
1
1
2
3
5
8
>>> i=5*9
>>> print("Value of i=",i)
Value of i= 45
>>> w=i/2
>>> print("W value is=",w,"I value is=",i)
W value is= 22.5 I value is= 45
>>> 
