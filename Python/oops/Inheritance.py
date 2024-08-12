# #Single Inheritance
# #parant class
# class person:
#     def __init__(self,name,contact):
#         self.name = name
#         self.contact = contact
    
#     def address(self):
#         print(self.name,self.contact)

# #child class
# class doctor(person):
#     pass

# class patient(person):
#     pass

# doc1 = doctor("Chinthu",9745474547)
# pat1 = patient("Sanju",8547947368)

# doc1.address()
# pat1.address()

# print()
# #Multilevel Inheritance
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Mammal(Animal):
#     def walk(self):
#         print("Mammal walks")

# class Dog(Mammal):
#     def bark(self):
#         print("Dog barks")

# # Example usage
# dog = Dog()
# dog.speak()  # Output: Animal speaks
# dog.walk()   # Output: Mammal walks
# dog.bark()   # Output: Dog barks

# print()
#Multiple Inheritance
class Walkable:

    def __init__(self):
        print("Walkable")

    def walk(self):
        print("Walking1")

class Swimmable:

    def __init__(self):
        print("Swimmable")

    def swim(self):
        print("Swimming")
    
    def walk(self):
        print("Walking2")

class Amphibian(Walkable, Swimmable):
    pass

# Example usage
frog = Amphibian()
frog.walk()
# frog.swim()

