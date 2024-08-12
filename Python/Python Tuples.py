thistuple = ("apple", "banana", "cherry")

print(thistuple)

print(thistuple[1])

y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)