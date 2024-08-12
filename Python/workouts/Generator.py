# In Python, generators are a type of iterable, like lists or tuples. 
# However, unlike lists, generators do not store their contents in memory.
# Instead, they generate values on the fly and yield them one at a time,
# which makes them much more memory efficient, especially when dealing 
# with large datasets or streams of data.

def my_generator(input_list):
    for i in input_list:
        yield i

gen = my_generator([1, 2, 3, 4, 5])
for value in gen:   
    print(value)




def generator(list):
    for i in list:
        if i%2 != 0:
            yield i

list = [1, 2, 3, 4, 5]
data = generator(list)
for i in data:
    print(i,end=" ")
