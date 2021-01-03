
class Student:

    school ="ABCDDD"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):#instance method due to self
        return (self.m1+self.m2+self.m3) /3

    # Accessors - Fetch Mutators -Modify
    def get_m1(self):
        return self.m1;
    def set_m1(self, value):
        self.m1= value

    @classmethod
    def getSchool(cls):
        return cls.school;

    @staticmethod
    def info():
        print("Static methods")


s1 = Student(14,45,67)
s2 = Student(33,34,67)

print(s1.avg())
print(s2.avg())

print(Student.getSchool())

print(Student.info())


