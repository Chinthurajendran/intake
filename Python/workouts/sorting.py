# list = [ 1,5,4,8,7,6,10,2]
# for i in range(0,len(list)):
#     for j in range(i+1,len(list)):
#         if list[i] > list[j]:
#             temp = list[i]
#             list[i] = list[j]
#             list[j] = temp
# print(list)

list = [ 1,5,4,8,7,6,10,2]

for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]
print(list)
