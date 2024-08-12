class A:
    def display(self):
        print("A")
class B:
    def display(self):
        print("B")
class c(B,A):
        pass

d= c()
d.display()
d.display()