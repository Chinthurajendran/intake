# def smart(func):
#     def inner(x,y):
#         return func(x,y/2)
#     return inner
# @smart
# def add(x,y):
#     print(x+y)

# add(5,2)

# def smart(func):
#     def inner(x,y):
#         return func(x,-y)
#     return inner
# @smart
# def add(x,y):
#     print(x+y)
# add(5,2)

# def smart(func):
#     def inner(x,*y):
#         return func(x,*y)
#     return inner
# @smart
# def add(x,y):
#     print(x+y)

# add(5,2)


# def logic(func):
#     def innert(name):
#         name = name.upper()
#         return func(name)
#     return innert

# @logic
# def text(name):
#     print(name)

# text("Chinthu")


# def wapper(func):
#     def inner(name):
#         result = name.upper()
#         return func(result)
#     return inner

# @wapper
# def text(name):
#     print(name)

# data = text('chinthu')

def wapper(func):
    def inner():
        x = func()
        return x*x
    return inner
@wapper
def num(): 
    return 10

print(num())

def wapper(func):
    def inner(num1, num2):
        x = func(num1, num2)
        return x * x
    return inner

@wapper
def add(num1, num2):
    return num1 + num2

result = add(3, 4)
print(result)  


