
for i in range(4):
    for k in range(i+1):
        print("#", end=" ")
    print()

print("Next")
for i in range(4):
    for k in range(4-i):
        print("#", end=" ")
    print()

print("Next")
for i in range(1,5):
    for k in range(i, 5):
        print(k, end=" ")
    print()