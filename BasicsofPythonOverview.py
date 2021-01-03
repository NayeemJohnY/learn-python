Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Script Start
>>> print("Nayeem")
Nayeem
>>> a=10;
>>> a="Nayeem"
>>> a
'Nayeem'
>>> nums=[]
>>> nums
[]
>>> mums=[10,20,"JOhn", a)
SyntaxError: invalid syntax
>>> nums=[10,20,"JOhn", a]
>>> mums
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    mums
NameError: name 'mums' is not defined
>>> nums
[10, 20, 'JOhn', 'Nayeem']
>>> nums.append(60)
>>> nums
[10, 20, 'JOhn', 'Nayeem', 60]
>>> nums.insert(2,"SDET)
	    
SyntaxError: EOL while scanning string literal
>>> nums.insert(2,"SDET")
>>> nums
[10, 20, 'SDET', 'JOhn', 'Nayeem', 60]
>>> nums.pop
<built-in method pop of list object at 0x0364D4B8>
>>> nums
[10, 20, 'SDET', 'JOhn', 'Nayeem', 60]
>>> nums.index("Nayeem":)
SyntaxError: invalid syntax
>>> nums.index("Nayeem")
4
>>> name=input("Print Name:  ")
Print Name:  Nayeeem
>>> print(name)
Nayeeem
>>> num1=int(input("Number"))
Number5
>>> num2=int(input("Number 2"))
Number 2gsd
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    num2=int(input("Number 2"))
ValueError: invalid literal for int() with base 10: 'gsd'
>>> num3=input("char")
chardoll
>>> num1*num3
'dolldolldolldolldoll'
>>> num3*num1
'dolldolldolldolldoll'
>>> num3***num1
SyntaxError: invalid syntax
>>> num3**num1
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    num3**num1
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> 5**num1
3125
>>> 5**num3
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    5**num3
TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
>>> 5*num3
'dolldolldolldolldoll'
>>> 5*num1
25
>>> 3125/5
625.0
>>> 3**num1
243
>>> 2**num1
32
>>> #ABove are power function
>>> n=10
>>> if n>0
SyntaxError: invalid syntax
>>> n="anyeem"
>>> if n>0:
	print("N is NUmber")

	
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    if n>0:
TypeError: '>' not supported between instances of 'str' and 'int'
>>> n=10
>>> if n>0:
	print("n is Number")
elif n%2==0:
	print ("Num is even")
else:
	print("Num is oddd")
else:
	
SyntaxError: invalid syntax
>>> n=10
>>> if n>0:
	print("n is Number")
elif n%2==0:
	print ("Num is even")
else:
	print("Num is oddd")
	
SyntaxError: multiple statements found while compiling a single statement
>>> if n>0:
	print("n is Number")
elif n%2==0:
	print ("Num is even")
else:
	print("Num is oddd")

	
n is Number
>>> n=-5
>>> f n>0:
	print("n is Number")
elif n%2==0:
	print ("Num is even")
else:
	print("Num is oddd")
	
SyntaxError: invalid syntax
>>> if n>0:
	print("n is Number")
elif n%2==0:
	print ("Num is even")
else:
	print("Num is oddd")

	
Num is oddd
>>> n=8
>>> if n>0:
	print("n is Number")
elif n%2=0:
	print ("Num is even")
else:
	print("Num is oddd")
	
SyntaxError: invalid syntax
>>> if n>0:
	print("n is Number")
elif n%2==0:
	print ("Num is even")
else:
	print("Num is oddd")

	
n is Number
>>> def fun1():
	print("Nayeem")
	print("John")

	
>>> fun1()
Nayeem
John
>>> fun2():
	
SyntaxError: invalid syntax
>>> def fun2( num):
	print(num)

	
>>> fun2()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    fun2()
TypeError: fun2() missing 1 required positional argument: 'num'
>>> fun2(5)
5
>>> for step in range(10):
	print(step)

	
0
1
2
3
4
5
6
7
8
9
>>> 
