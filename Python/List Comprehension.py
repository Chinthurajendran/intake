fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

new = [x for x in range(10)]
print(new)

new = [x for x in range(10) if x < 4]
print(new)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new = [x.upper() for x in fruits]
print(new)

new = [x.lower() for x in fruits if x != "kiwi"]
print(new)

new = ["chinthu" for x in fruits]
print(new)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
