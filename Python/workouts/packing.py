def func(a, b, c):
    print(a, b, c)

args = (1, 2, 3)
func(*args)  # Unpacks the tuple into arguments

def func(a, b, c):
    print(a, b, c)

kwargs = {'a': 1, 'b': 2, 'c': 3}
func(**kwargs)  # Unpacks the dictionary into keyword arguments

def func(*args):
    print(args)

func(1, 2, 3)  # args is a tuple (1, 2, 3)


def func(**kwargs):
    print(kwargs)

func(a=1, b=2, c=3)  # kwargs is a dictionary {'a': 1, 'b': 2, 'c': 3}
