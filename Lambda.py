


add = lambda a, b : a+b
print(add(7, 8))

square = lambda a : a*a
print(square(4))

from functools import reduce

nums = [4,5,6]

print(list(filter(lambda n : n%2==0, nums)))

print(list(map(lambda n : n*2, nums)))

print(reduce(lambda a,b : a+b, nums))

