#Overloading
class name:

    def num(self,a,b,c=0):
        print(a+b+c)

k = name()
k.num(1,2)

#Overriding

class A:
    def name(self):
        print("Class A")

class B(A):
    def name(self):
        print("Class B")
        super().name()

k = B()
k.name()