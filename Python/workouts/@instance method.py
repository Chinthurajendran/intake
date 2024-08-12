class number:
    def __init__(self,value):
        self.instance_attribute = value
    
    def looping(self):
        self.instance_attribute +=1
        return self.instance_attribute 
    
obj = number(10)
print(obj.looping())
print(obj.looping())
print(obj.looping())
