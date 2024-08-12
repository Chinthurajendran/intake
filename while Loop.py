i = 1
while i < 6:
  print(i)
  i += 1


# def list(list):
#     for i in range(len(list)):
#         print(list[-i-1])
#         print(-i-1)


# new = [1,2,3,4,5]
# list(new)

def print_reversed_list(lst):
    i = len(lst)-1
    print(i)
    print()
    while i >=0:
        print(lst[i])
        i-=1
new = [1, 2, 3, 4, 5]
print_reversed_list(new)