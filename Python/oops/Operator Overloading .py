# class product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
    
#     def __add__(self,other):
#         final = self.price+p2.price
#         print(final)

# p1 = product("iphone",120000)
# p2 = product("Mac",142000)
# p1+p2


# from collections import Counter

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         # Count the frequency of each character in ransomNote and magazine
#         ransom_note_count = Counter(ransomNote)
#         magazine_count = Counter(magazine)

#         # Check if the magazine has enough of each character required by the ransom note
#         for char, count in ransom_note_count.items():
#             print(char)
#             print(count)
#             print(magazine_count[char])
#             if magazine_count[char] < count:
#                 return False
#         return True

# # Example usage:
# solution = Solution()
# print(solution.canConstruct("a", "b"))         # Output: False
# print(solution.canConstruct("aa", "ab"))       # Output: False
# print(solution.canConstruct("aa", "aab"))      # Output: True


class Parent1:
    def __init__(self):
        print("Sanju")

class Parent2:
    def __init__(self):
        print("Chinthu")

class Child(Parent1, Parent2):
    pass

data = Child()