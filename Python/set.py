"""
sets are similar to list but unordered and cannot contain duplicate values]
used for fast removal of duplication from list
"""


my_set = {1,2,3,4,5,6}
print(my_set)
print(type(my_set))
print(len(my_set))

for x in my_set:
    print(x)

# we cannot access like this because of the random storage of the element
# print(my_set[0])

# To remove any element
my_set.discard(4)
print(my_set)

# TO add a single element
my_set.add(4)

# To add multiple elements at the end of the set
my_set.update([7,8])
print(my_set)