a = 5
b = 0

try:
    print(a/b)
except Exception as e:
    print("Not Divisible by zero: ", e)
finally:
    print("Resource Closed")
print("good")

