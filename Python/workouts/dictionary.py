# Dictionary Comprehension Syntax
# {new_key: new_value for key, value in iterable}

text = {'a':1,'b':2,'c':3}
swap ={value : key for key , value in text.items()}
print(swap)

# -----------------------------------------------------------------------------------------------------------------------------------
print()
original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

new_dict = {}

for key, value in original_dict.items():
    if value not in new_dict.values():
        new_dict[key] = value
print(new_dict)

# -----------------------------------------------------------------------------------------------------------------------------------
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)

print()

for x in thisdict:
  print(thisdict[x])

print()

for x in thisdict.values():
  print(x)

print()

for x in thisdict.keys():
  print(x)

print()

for x, y in thisdict.items():
  print(x, y)