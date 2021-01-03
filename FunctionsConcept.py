

def greet():
    print("hello")


greet()

def add(x, y):
    print(x+y)

add(4,5)

def sub(x, y):
    return x-y

print(sub(5,8))

def add_sub(x,y):
    return x+y, x-y

print(add_sub(5,8))

def update(x):
    print(id(x))
    x = 10
    print(id(x))
    print("x : ", x)

a = 5;
print(id(a))
update(a)
print(a)
print(id(a))

def update(x):
    print(id(x))
    x[2] = 10
    print(id(x))
    print("x : ", x)

a = [5, 7, 8];
print(a)
print(id(a))
update(a)
print(a)
print(id(a))


def person(name, age):
    print(name)
    print(age-4)

person("nayeem", 24)#position
#person(24, "Nayeem")
person(age=23, name="John")#keyowrd

def person(name, age =18):
    print(name)
    print(age-4)

person("nayeem")#Default


#Variable length
def sum(a, *b):
    for i in b:
        a+=i
    print(a)

sum(56,5,16,7)

#keyword variable length
def person(name, **data):
    print(name)
    print(data)
    for i, j in data.items():
        print(i, j) #key value pair

person('Nayeem', Age=26, Role="SDET", City ="BLR")


#Scope
a = 10 #Global

def something():
    global a
    a = 15 #local
    #globals("a")# change global without effecting local use globals function
    print(a)

something()
print(a)

def count(list):
    even = 0
    odd = 0
    for i in list:
        if i% 2 == 0:
            even+=1
        else :
            odd+=1

    return even, odd


list = [2,4,5,3,644,555,77,88,9]
even , odd = count(list)
print("Even : {} and odd {}".format(even , odd))