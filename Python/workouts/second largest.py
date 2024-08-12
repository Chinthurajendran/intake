list = [1,2,3,4,5,6,7,8,9,10]
largest = 0
seocnd_largest = 0

for i in list:
    if i > largest:
        seocnd_largest = largest
        largest = i
    elif i > seocnd_largest  and seocnd_largest != largest:
        seocnd_largest = largest

print(largest)
print(seocnd_largest)

