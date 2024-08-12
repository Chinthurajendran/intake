# original_dict = {1: 1, 2: 2, 3: 3, 4: 4}
# new = {value: value for value in original_dict.values()}
# new = {key**3:value**2 for key,value in new.items()}
# print(new)

# swap = {value:key for key,value in new.items()}
# print(swap)

# def flatten(lst):
#     flattened_list = []
#     for item in lst:
#         if isinstance(item, list):
#             flattened_list.extend(flatten(item)) 
#             print(flattened_list)
#         else:
#             flattened_list.append(item)
#     return flattened_list

# my_list = [1, 2, [3, 4, [5, 6]]]
# flattened_list = flatten(my_list)




# print(flattened_list)
# #output
# [1, 2, 3, 4, 5, 6]

# name = 'chinthu'
# new = list(name)
# new[0]='k'
# data = ''.join(new)
# print(data)

# name  ='chinthu'
# dict = {}
# for i in range(len(name)):
#     count = 0
#     for j in name:
#         if name[i] == j:
#             count+=1
#     dict[name[i]] = count
# print(dict)
# max_value = max(dict.values())
# print(max_value)
# new = [key for key, value in dict.items() if value == max_value]
# print(new)

    # Students = [("student", 12, 25, 56),
    #             ("student2",32,45, 65),
    #             ("student3", 302,45, 65)]

    # person = None
    # height_avg = None
    # for i in Students:
    #     avarage = (i[1]+i[2]+i[3])//3
    #     if person is None:
    #         person = i[0]
    #         height_avg = avarage
    #     elif avarage > height_avg:
    #         height_avg = avarage
    #         person = i[0]
    # print(person)
    # print(height_avg)


# def my_list(lists):
#     new = []
#     for item in lists:
#         if isinstance(item,list):
#             new.extend(my_list(item))
#         else:
#             new.append(item)
#     return new

# s = [1, 2, [3, 4, [5, 6]]]
# data = my_list(s)
# print(data)

# s = [[1, 2], [3, 4], [5, 6]]

# new = [element for sublist in s for element in sublist]
# print(new)

# def sum_of_numbers(numbers):
#     total_sum = 0
#     print(numbers)
#     for num in numbers:
#         print(num)
#         total_sum += num
#     return total_sum
# 1

# # # Example usage:
# # n = 5  # Number of elements (adjust as needed)
# # numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
# numbers =[int(input('numbers:')) for i in range(5)]
# # Call the function and print the result
# print("Sum of numbers:", sum_of_numbers(numbers))

# number = [1,2,3,4,5]
# dict = {}

# for i in range(len(number)):
#     dict[number[i]] = number[i]
# print(dict)

# number = [1,2,3,4,5]
# dict = {number[i]:'even' if number[i]%2 == 0 else 'odd' for i in range(len(number))}
# print(dict)

number = {1,2,3,4,5,6}
number_list = list(number)
index = number_list.index(3)
value = number_list[-1]

number_list.remove(3)
number_list.remove(6)
number_list.insert(index,value)
print(number_list)
data = set(number_list)
print(data)