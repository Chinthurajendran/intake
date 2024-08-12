# num = 153
# digits = str(num) 
# length = len(digits)
# nums = []
# for i in digits:
#     for j in range(length):
#         sum = i*i
#         print(sum)
# 1*1*1 + 5*5*5 + 3*3*3 = 153
# When we use int(digit) ** length, it means raising the integer value of digit to the power of length.

# num = 153
# digits = str(num) 
# length = len(digits)
# print(length)
# sum_of_powers = 0

# for digit in digits:
#     sum_of_powers += int(digit) ** length
#     print(sum_of_powers)

# if sum_of_powers == num:
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")


num = 1634
digit = str(num)
length = len(digit)
sum = 0
for i in digit:
    sum += int(i)**length
print(sum)


num = 1634
num_str = str(num)
lenght = len(num_str)
sum = 0
for i in num_str:
    sum+= int(i)**lenght
print(sum)