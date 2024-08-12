class person:

    def __init__(self,name,age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def set_name(self,name):
        self._name = name
    
    def set_age(self,age):
        self._age = age


data = person("Alice", 30)
print(data.get_name())
print(data.get_age())

data.set_name("chinthu")
data.set_age(20)

print(data.get_name())
print(data.get_age())


class info:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def getter(self):
        print(self.name,self.age)
    
    def setter(self,name,age):
        self.name = name
        self.age=age

txt = info('chinthu',26)
txt.getter()
txt.setter('sanju',31)
txt.getter()
