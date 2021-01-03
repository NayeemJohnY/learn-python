
class Student:
    def __init__(self, name, rollno):
        self.name =name
        self.rollno = rollno
        self.lap = self.laptop()
    def show(self):
        print(self.name, self.rollno)

    class laptop:
        def __init__(self):
            self.brand = "HP"
            self.ram ="4GB"

        def show(self):
            print(self.brand, self.ram)

s1 = Student("naveenn", 23)
s2 = Student("Gopi", 33)

s1.show()
print(s1.lap.brand)
print(id(s1.lap))
print(id(s2.lap))
lap = Student.laptop()
lap.show()