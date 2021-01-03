#Adding additional meaning to the existing function

def div(a,b):
    print(a/b)


def smart_div(func):

    def inner(a,b):
        if a< b:
            a,b = b, a
            return func(a,b)
    return inner

div(4,5)

div = smart_div(div)

div(4,5)

#Modules
from FindLargestNumber import largest

largest()

#special variable name

print(__name__)