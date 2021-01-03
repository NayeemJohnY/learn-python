Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(false==0)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(false==0)
NameError: name 'false' is not defined
>>> print(False==0)
True
>>> print(True==0)
False
>>> print(True)
True
>>> print(True+False)
1
>>> print(True+True+False)
2
>>> print(True and True)
True
>>> print(True and False)
False
>>> print(True and True and False)
False
>>> print(False and False or True)
True
>>> 3 and 0
0
>>> 30 and 10
10
>>> 3 and 10
10
>>> 3 and 7
7
>>> 7 and 3
3
>>> 7 or 3
7
>>> 3 or7
SyntaxError: invalid syntax
>>> 3 or  7
3
>>> 12 or 13
12
>>> 011 or 111
SyntaxError: invalid token
>>> 11 or 111
11
>>> 11 and 111
111
>>> print (None == 0) 
  
# showing objective of None 
# two None value equated to None 
# here x and y both are null 
# hence true 
x = None
y = None
print (x == y) 
  
# showing logical operation  
# or (returns True) 
print (True or False) 
  
# showing logical operation  
# and (returns False) 
print (False and True) 
  
# showing logical operation  
# not (returns False) 
print (not True)
SyntaxError: multiple statements found while compiling a single statement
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> clear
No Python documentation found for 'clear'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> print(None==0)
False
>>> print(None)
None
>>> print(None==1)
False
>>> assert(True==False)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    assert(True==False)
AssertionError
>>> assert(True==True)
>>> print(assert(True==True))
SyntaxError: invalid syntax
>>> assert(5>0)
>>> assert(9<0)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    assert(9<0)
AssertionError
>>> a=[10,15,14]
>>> a
[10, 15, 14]
>>> del a[1]
>>> a
[10, 14]
>>> del[3]
SyntaxError: can't delete literal
>>> del a[3]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    del a[3]
IndexError: list assignment index out of range
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> if 'i' in "geeks":
	print("i si present")
else : print("I is not present")

I is not present
>>> for i in "geeks":
	print(i)

	
g
e
e
k
s
>>> for i in "geeks":
	print(i, end='')

	
geeks
>>> 
>>> print("\r")

>>> print("\n")


>>> print(' 'is ' ')
True
>>> print({} is {})
False
>>> print 'a' is 'a')
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('a' is 'a'))?
>>> print 'a' is 'a')
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('a' is 'a'))?
>>> print ('a' is 'a')
True
>>> a=10;
>>> def mod1():
	print(a)

	
>>> def mod2():
	a=15

	
>>> def mod3():
	global a=20
	
SyntaxError: invalid syntax
>>> def mod3():
	global a
	a=20

	
>>> mod1()
10
>>> mod2()
>>> mod1()
10
>>> mod3()
>>> mod1()
20
>>> a
20
>>> print ("Value of a using nonlocal is : ",end="")
Value of a using nonlocal is : 
>>> def outer():
	b=7
	def inner():
		nonlocal a
		
SyntaxError: no binding for nonlocal 'a' found
>>> def outer():
	b=7
	def inner():
		nonlocal b
		b=14
	inner()
	print(a)

>>> outer()
20
>>> def outer():
	b=7
	def inner():
		nonlocal b
		b=14
	inner()
	print(b)

	
>>> outer()
14
>>> def outer():
	c=7
	def inner():
		c=14
	inner()
	print(b)

	
>>> outer()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    outer()
  File "<pyshell#96>", line 6, in outer
    print(b)
NameError: name 'b' is not defined
>>> def outer():
	c=7
	def inner():
		nonlocal b
		c=14
	inner()
	print(c)
	
SyntaxError: no binding for nonlocal 'b' found
>>> def outer():
	c=7
	def inner():
		c=14
	inner()
	print(c)

	
>>> outer()
7
>>> inner()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    inner()
NameError: name 'inner' is not defined
>>> outer().inner()
7
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    outer().inner()
AttributeError: 'NoneType' object has no attribute 'inner'
>>> def outer():
	b=7
	def inner():
		b=14
		print(b, "in inner")
inner()
	print(b)
	
SyntaxError: invalid syntax
>>> def outer():
	b=7
	def inner():
		b=14
		print(b)
	inner()
	print(b)

	
>>> outer()
14
7
>>> 
