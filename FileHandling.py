

f = open("MyData.txt","r")
print(f)

#print(f.read())
#print(f.readline())
#print(f.readline())
#print(f.readline(4))
f1 = open("abc.txt", "w")
for data in f:
    f1.write(data)