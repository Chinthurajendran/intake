thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
  print(x)

thisset.add("orange")

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

myset = set1.union(set2, set3, set4)
print(myset)
