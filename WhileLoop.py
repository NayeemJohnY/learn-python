i = 1

while i <= 100:
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    i += 1

x = '#'
i = 0
while i < 4:
    j = 0
    while j < 4:
        print(x, end=" ")
        j += 1
    i += 1
    print()