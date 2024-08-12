class Resource:
    def __init__(self, name):
        self.name = name
        print(f'Resource {self.name} created')

    def __del__(self):
        print(f'Resource {self.name} destroyed')

resource = Resource("FileHandler")
del resource


class text:
    def __init__(self):
        self.name  = 'chinthu'
        print(self.name)
    
    def __del__(self):
        print("destructor")

txt = text()
del text