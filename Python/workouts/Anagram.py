a = 'geeksforgeeks'
b = 'forgeeksgeeks'

if len(a)==len(b) and sorted(a) == sorted(b):
    print("it is Anagram")
else:
    print("it is not Anagram")


list = ['tea','eat']
str1_sorted = sorted(list[0])
str2_sorted = sorted(list[1])
if str1_sorted == str2_sorted:
    print('True')
else:
    print('False')