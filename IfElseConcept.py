
x = 6

if x % 2 == 0:
    print("Even")
    if x > 10:
        print("Greater than 10")
    elif x % 3 == 0:
        print("less than 10 & Divisible by 3")
    else:
        print("Not divisible by 3 and less than 10")
else:
    print("odd")