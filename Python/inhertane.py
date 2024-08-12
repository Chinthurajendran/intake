class A:
    def name(self):
        print("A")

class B:
    def name(self):
        print("B")

class C(A,B):
    pass

data = C()
data.name()