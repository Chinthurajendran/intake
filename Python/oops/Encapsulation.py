class new:
    def __init__(self):
        self.a = 10 #PUBLIC
        self._b = 20 #PRIVATE
        self.__c = 30 #PROTECTED
    
    def print(self):
        print(self.__c)

a = new()

print(a.a,a._b)
a.print()