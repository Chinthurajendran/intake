num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime = []

# for i in num:
#     if i > 1: 
#         flag = True
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 flag = False
#                 break
#         if flag:
#             prime.append(i)

# print(sorted(prime))

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime = []

for i in num:
    if i > 1:  # 1 is not a prime number
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(i)

print(prime)



new = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num)
            return False
    return True

# Finding prime numbers using a for loop
prime_numbers = []
for num in new:
    if is_prime(num):
        prime_numbers.append(num)

print(prime_numbers)



# def prime(num):
#     data = [i for i in range(2,num) if num%i != 0]
#     prime(data)


# new = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in new:
#     data= prime(i)

# new = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def prime(num):
#     if num < 2:
#         return []
#     data = [i for i in range(2, num) if num % i != 0]
#     return data

# for i in new:
#     data = prime(i)
# print(data)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

new = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]
prime = [ num for num in new if all(num%i != 0 for i in range(2,num)) and num >1]
print(prime)


new = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]
prime = [num for num in new if all(num%i != 0 for i in range(2,num)) and num>1]
print(prime)    


