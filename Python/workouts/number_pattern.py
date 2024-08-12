k = 1
for i in range(5):
    for j in range(i+1):
        print(k,end=" ")
        k+=1
    print()

print()

for i in  range(5):
    for j in range(i+1):
        print(i-j+1,end=" ")
    print()

print()

for i in range(5):
    for j in range(i+1):
        print(5-i+j,end=" ")
    print()