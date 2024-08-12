# In Python, an iterator is an object that can be iterated upon 
# (i.e., it allows you to traverse through all the values). 
# An iterator object implements 
# two special methods: __iter__() and __next__().


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))