# list = [1, 2, 3, 4, 5, 6]

# for i in range(len(list)):
#     print(list[-i-1])
# print()


# list = [1, 2, 3, 4, 5, 6]
# i = 0
# while i < len(list):
#     print(list[-i-1])
#     i += 1

# print()


# name = 'chinthu'
# if len(name) > 2:
#     first = name[0].upper()
#     mid = name[1:-1]
#     last = name[-1].upper()
#     result = first + mid + last
# print(result)


class parant:
    def __init__(self):
        self.data = 'chinthu'
class child(parant):
    def __init__(self):
        super().__init__()
        a = self.data
        print(a)
    
data = child()
