# 5×4×3×2×1=120

# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num*factorial(num-1)

# print(factorial(5))


def sum(my_list):
    if not my_list:
        return 0
    else:
        return my_list[0]+sum(my_list[1:])

my_list = [1, 2, 3, 5, 4, 5]

total = sum(my_list)
print(total)
