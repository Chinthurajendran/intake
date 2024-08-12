# myDict = {'ravi': 10, 'rajnish': 9,
#         'sanjeev': 15, 'yash': 2, 'suraj': 32}

# key  = list(myDict.keys())
# print(key)
# sorted_dict = {i:myDict[i] for i in key}

# print(sorted_dict)
# print()

# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}


# new_dict= dict1.copy()
# new_dict.update(dict2)
# print(new_dict)

# dict1.update(dict2)


# print(dict1)

# n = 19
# dighit = str(n)
# k = dighit
# while len(k) >1:
#     sum = 0
#     for i in k:
#         for j in k:
#             sum+= int(i)+int(j)
#         k = str(sum)
# print(k)

# print("chinthu")

# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# new = []
# for i in s:
#     if i not in new:
#         new.append(i)
# print(new)
# print(len(new))

# lists = [1, 2, 3, [5, 6]]

# # Reverse each nested list inside the original list
# reversed_lists = [sublist[::-1] if isinstance(sublist, list) else sublist for sublist in lists[::-1]]

# # Print the final reversed list
# print(reversed_lists)

# lists = [1, 2, 3, [5, 6]]
# for i in range(len(lists)):
#     if isinstance(lists[i],list):
#         lists[i] = lists[i][::-1]
# print(lists[::-1])

d ={'a':[1,2,3],'b':[4,6],'c':10}

for key,value in d.items():
    if isinstance(value,list):
        d[key] =  sum(value)
    else:
        d[key] = value 

print(d)  
