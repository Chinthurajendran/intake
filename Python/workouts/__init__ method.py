class main:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printer(self):
        print("Address is :",self.name,self.age)

data = main("Chinthu",28)

data.printer()


class main:
    def __init__(self,name,address):
        self.name = name
        self.address = address
    
    def display(self):
        print(self.name,self.address)

text = main('chinthu','ernakulam')
text.display()
