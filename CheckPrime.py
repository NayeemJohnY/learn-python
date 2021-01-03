num = 5
isPrime = True
for i in range(2, num):
    if num % i == 0:
        isPrime = False
        break;
if(isPrime):
    print(num, "Number is prime")
else:
    print(num, "Number is not prime")

def fun():
    pass

a = 34