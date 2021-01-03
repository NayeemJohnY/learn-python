

class Computer:
    def __init__(self):
        print("In init")
    def config(self):
        print("ig 16GB")

comp1 = Computer()

print(type(comp1))

#Computer.config()
comp1.config()
Computer.config(comp1)

comp2 = Computer()


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("name : ", self.name, "age : ", self.age)


per = Person("Nayeem",25)
per.display()


#compare 2 objects
#self.name == other.name