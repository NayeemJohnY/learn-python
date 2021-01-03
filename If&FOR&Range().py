Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=int(input("Enter NUmber"))
Enter NUmber9
>>> if x>0:
	print(x)
	elif x%2==0
	
SyntaxError: invalid syntax
>>> elif x%2==0:
	
SyntaxError: invalid syntax
>>> if x>0:
	print(x)
	elif x%2==0:
		
SyntaxError: invalid syntax
>>>  if x>0:
	print(x)
elif x%2==0:
	
SyntaxError: unexpected indent
>>> x=int(input("Enter NUmber"))
Enter NUmber 5
>>> if x>0:
	print(x)
elif x%2==0:
	print(x,"Number is Even")
elif x>5==0:
	print(x,"Number is greater 5")
	else :
		
SyntaxError: invalid syntax
>>> if x>0:
	print(x)
elif x%2==0:
	print(x,"Number is Even")
elif x>5==0:
	print(x,"Number is greater 5")
else:
	print("Good Bye",x)

	
5
>>> x=9
>>> 
>>> if x>0:
	print(x)
elif x%2==0:
	print(x,"Number is Even")
elif x>5==0:
	print(x,"Number is greater 5")
else:
	print("Good Bye",x)

	
9
>>> x=-5
>>> if x>0:
	print(x)
elif x%2==0:
	print(x,"Number is Even")
elif x>5==0:
	print(x,"Number is greater 5")
else:
	print("Good Bye",x)

	
Good Bye -5
>>> x=-4
>>> if x>0:
	print(x)
elif x%2==0:
	print(x,"Number is Even")
elif x>5==0:
	print(x,"Number is greater 5")
else:
	print("Good Bye",x)

	
-4 Number is Even
>>> words=['Nayeem', 'John','SDET']
>>> for w in words
SyntaxError: invalid syntax
>>> for w in words:
	print(w,len(w))

	
Nayeem 6
John 4
SDET 4
>>> words[:]:
	
SyntaxError: invalid syntax
>>> words[:]
['Nayeem', 'John', 'SDET']
>>> words.insert(-1,"Cengage")
>>> words
['Nayeem', 'John', 'Cengage', 'SDET']
>>> words(4,Cognizant)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    words(4,Cognizant)
NameError: name 'Cognizant' is not defined
>>> words.append(3."Cognizant")
SyntaxError: invalid syntax
>>> words.append(3,"Cognizant")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    words.append(3,"Cognizant")
TypeError: append() takes exactly one argument (2 given)
>>> words.append("Cognizant")
>>> words
['Nayeem', 'John', 'Cengage', 'SDET', 'Cognizant']
>>> for i in range(10):
	print(i)

	
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
>>> range(5,10)
range(5, 10)
>>> for i in range(len(words)):
	print(i words[i])
	
SyntaxError: invalid syntax
>>> 
>>> for i in range(len(words)):
	print(i,words[i])

	
0 Nayeem
1 John
2 Cengage
3 SDET
4 Cognizant
>>> list(range(10,80))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
>>> 
