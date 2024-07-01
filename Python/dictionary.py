"""
Dictionary
"""

user ={
    'username':"codewithshivam",
    'first':'shivam',
    'last':'Pandey',
    "age":20

}

# Add new key value pairs
user["married"] = False
print(user)
print(len(user))

user.pop("last")
print(user)



for x in user:
    print(x)

for x,y in user.items():
    print(x,y)



user2= user
user2.pop("age")
# Here the alge will also be gone because of the memory allocvaton of the python both are pointing to the 
# same memory location
print(user)

#To handle that we use .copy()
user3 = user.copy()
user3.pop("first")
print(user3)


# cleared the dictionary
user.clear()
print(user)



#Delete the dictonary form the memory
del user
# Here we will get name error 
# print(user)

