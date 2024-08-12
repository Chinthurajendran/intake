# Copy by value

a = 5
b = a
b = 10

print(a)
print(b)

# copy by reference

a = [1,2,3,4]
b = a
b.append(5)
print(a)
print(b)