class main:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        value = self.x+other.x+self.y+other.y
        print(value)


data = main(1,2)
data1 = main(2,1)

data+data1