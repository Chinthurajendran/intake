# Unpacking iterables into function arguments
def func(a,b,c):
    print(a,b,c)

data = (1,2,3)
func(*data)

# Unpacking dictionaries into function keyword arguments
def func(a,b,c):
    print(a,b,c)

data = {'a':1,'b':2,'c':3}
func(**data)

# packing iterables into function arguments
def func(*data):
    print(data)

func(1,2,3)

# packing dictionaries into function keyword arguments
def func(**data):
    print(data)

func(a=1,b=2,c=3)