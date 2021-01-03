from array import *
import math

vals = array("i", [7,8,9,9,7,6])
print(vals)

for e in vals:
    print(e)

vals.insert(3,5)
print(vals)

print(vals.typecode)

vals.reverse()
print(vals)

newArr = array(vals.typecode, (a*a for a in vals))
print(newArr)


print(sorted(vals))

print(math.factorial(5))

arr = array("i", [])

for i in range(1,6):
    arr.append(i*5)

print(arr)

print(arr.index(20))

del arr[2]
print(arr)

#reverse an array
reverse = array(arr.typecode, [])
for a in range(len(arr)-1,-1, -1):
    reverse.append(arr[a])

print("Reverse", reverse)
#Multi dimensional array is not supported by inbuilt python
