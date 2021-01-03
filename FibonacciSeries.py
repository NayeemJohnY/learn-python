
a = 0
b = 1;
for i in range(5):
    print(a)
    a, b = b, a+b

print("Trial")
a = 0
b = 1
for i in range(5):
     c= a +b
     a =b
     b = c
     print(c)


#factorial
def fact(x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i

    print(factorial)


fact(5)

import sys
print("Recursion Limit" ,sys.getrecursionlimit())
#Recursive
def factorial(x):
    if x == 1:
        return 1
    return x*factorial(x-1)
print(factorial(5))