# #Filter
num = [1,5,8,7,4,2]
new = list(filter(lambda a :a%2==0,num))
print(new)

words = ["apple", "banana", "cherry", "date"]

new = list(filter(lambda x : "a" in x,words ))
print(new)

# #Map

# In Python, the map() function is a built-in function used to apply a 
# given function to all the items in an iterable (such as a list, tuple, or dictionary) 
# and returns a new iterator that yields the results.

num = [1,5,8,7,4,2]
new = list(map(lambda a : a*2,num))
print(new)

num = [1,5,8,7,4,2]
for index,value in enumerate(num):
    print(f'{index}:{value}')

