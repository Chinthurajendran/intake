class myclass:
    name = 'chinthu'  # Class attribute

    def __init__(self, data):
        self.data = data  # Correctly initialize the instance attribute
        print(myclass.name)  # Access the class attribute using the class name or self.name
    
    def display(self):
        print(self.data)
        print(myclass.name)  # Access the class attribute using the class name or self.name

# Example usage
obj = myclass('some data')
obj.display()
