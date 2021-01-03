from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod #At least one abstarct method
    def name(self):
        pass

class laptop(Computer):
    def name(self):
        print("In laptop")
    def display(self):
        print("Hei")
c1 = laptop()
c1.name();

# Iterator
nums = [5,6,7,89]
it = iter(nums)
print(it.__next__())


#Generator
def gen(x):
    for i in range(1,x+1):
        yield i*i
x = gen(5)
print(x.__next__())
print(x.__next__())
print(x.__next__())