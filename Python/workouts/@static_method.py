class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):  
        return x - y

# Calling static methods
result_add = MathOperations.add(5, 3)        # 8
result_subtract = MathOperations.subtract(5, 3)  # 2

print(result_add)       # Output: 8
print(result_subtract)  # Output: 2
