def largest():
    print("Module ", __name__)
    x, y, z = 1789, -201, 67
    if x >y and x > z:
        print(x)
    elif y > z:
        print(y)
    else:
        print(z)
if __name__ == "__main__":
    largest()