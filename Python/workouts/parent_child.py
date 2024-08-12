class A:
    def __init__(self,name):
        self.name = name
class B(A):
    def __init__(self,name):
        super().__init__(name)
        print(self.name)

data = B('chinthu')