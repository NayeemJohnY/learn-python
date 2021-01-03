

class Car:

    wheels =4 #Class variable
    def __init__(self):
        self.mil= 10 #instance varibale
        self.name ="BMW"


c1= Car()
c2 = Car()

print(c1.mil)
print(c2.mil)
print("Wheels", c1.wheels)

c1.mil = 56
c1.wheels = 8
print("Wheels", c1.wheels)
print("Wheels Using class ", Car.wheels)
Car.wheels = 10
print("Wheels Using class ", Car.wheels)
print(c1.mil)
print(c2.mil)