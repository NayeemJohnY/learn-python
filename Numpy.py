from numpy import *

arr = array([1, 2,3, 4,65], float)

print(arr)
print(arr.dtype)


arr = linspace(0, 5, 3)#parts
print(arr)


arr = arange(1, 15, 2 )#steps
print(arr)

arr = logspace(1, 14, 5)#log values
print(arr)

arr1 = zeros(5, int)
print(arr1)

arr2 = ones(4)
print(arr2)

arr1 = arr2 +4
print(arr1)


print(arr1+arr2)

print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(sort(arr))

print(concatenate([arr1, arr2]))

#copying array
a = array([2,3,4,5,6])
b =a
print(a)
print(b)

print(id(a))
print(id(b))

c = a.view() #shadow copy
print(a)
print(c)
print(id(c))


d = a.copy()
a[2] = 123
print(a)
print(d)
print(id(d))

#code to add arrary
numarray1 = array([3,4,5,6,7])
numarray2 = array([3,4,5,6,7])
for i in range(len(numarray1)):
    print(numarray1[i]+numarray2[i], end=" ")


# find max of arrray
max = numarray1[0]
for e in numarray1:
    if max < e:
        max = e
print("Max", max)


#Multi Dimensionla array

multi = array([
    [1, 2,3, 4, 4, 6],
    [4,5,6, 5, 4 ,3]
])
print(multi)
print(multi.dtype)
print(multi.ndim)
print(multi.shape)
print(multi.size)

#convert 2d to 1d
single = multi.flatten()
print(single)


two = single.reshape(3, 4);
print(two)

three = single.reshape(2,2, 3);
print(three)


m = matrix(multi)
print(diagonal(two))


