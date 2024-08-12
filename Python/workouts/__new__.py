class MyClass:
    def __new__(cls, *args, **kwargs):
        # Custom object creation logic
        instance = super().__new__(cls)  # Calling base class's __new__ method
        print("chinthu")
        # Additional initialization if needed
        return instance

    def __init__(self, value):
        self.value = value
        print(self.value)
        # Initialization code in __init__ method

# Creating an instance of MyClass
obj = MyClass(10)
