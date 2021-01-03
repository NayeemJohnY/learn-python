

class A:
    def __init__(self):
        print("in init A")

    def f1(self):
        print("f1")

    def f2(self):
        print("f2")


class B:
    def __init__(self):
        print("in init B")

    def f1(self):
        print("f1 in B")

    def f3(self):
        print("f3")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in init C")


obj = C();
obj.f1()