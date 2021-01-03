# Duck Typing
# Operator Overloading
# Method Overloading
# Method Overriding


# Duck Typing
class pyCharm:

    def execute(self):
        print("Compiling & Running")

class MyIde:

    def execute(self):
        print("Writing & Spell")
class Laptop:

    def code(self, ide):
        ide.execute()


ide = pyCharm();
lap = Laptop()
lap.code(ide)


ide = MyIde()
lap = Laptop()
lap.code(ide)




# Operator Overloading

a = 5
b = 6

print(a+b)
print(int.__add__(a,b))


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a, b):
        return a+b

    def sum(self, a, b, c):
        return a + b+ c

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1,m2)

    def __gt__(self, other):
        s1_marks = self.m1 + self.m2
        s2_marks = other.m1 + other.m2
        if s1_marks > s2_marks:
            return True
        else:
            return False

    def __str__(self):
        return "{} {}".format(self.m1, self.m2)

s1 = Student(10,40)
s2 = Student(10,45)


s3 = s1+s2
print(s3.m2)

print(s1 >s2)
print(s1.__str__())
print(s1)


# Method overloading
print(s1.sum(4,5,6,7))