from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def sleep(self):
        print("This animal is sleeping.")

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Bark
print(cat.speak())  # Output: Meow

dog.sleep()  # Output: This animal is sleeping.
cat.sleep()  # Output: This animal is sleeping.
