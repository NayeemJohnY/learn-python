nums = ["nayeem", 2, 4]

for i in nums:
    print(i)

for i in "Nayeem Welocme":
    print(i)

for i in range(12, 67, 3):
    print(i)

for i in range(52, 11, -1):
    print(i)

#Print perfect square number  between 1 to 500
import math
print("Perfect square numbers")
for i in range(1, 501):
    if math.sqrt(i) - int(math.sqrt(i)) == 0:
        print(i)