pos = -1

def search(list, n):
    i = 0;
    while i <len(list):
        if list[i] == n:
            globals()["pos"] = i
            return True;
        i += 1
    return False

list = [41, 4,89, 5,6 ,7 ,8, 9]
n = 8
if search(list, n):
    print("Found", pos+1)
else:
    print("False")

#Binary Search

def binarySearch(list, n):
    low = 0;
    upper = len(list) -1
    while low <= upper:
        mid = (low +upper) //2
        if list[mid]== n :
            globals()["pos"] = mid
            return True
        elif n > list[mid]:
            low = mid+1
        else:
             upper = mid -1





n = 9
list = sorted(list)
print(list)
if binarySearch(list, n):
    print("Found", pos+1)
else:
    print("False")
