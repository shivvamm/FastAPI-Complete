"""
List
"""

list = [45,6,54,6,43,5,3]
print(list)
print(list[0])
print(list[-1])
list.append(2000)
print(list)

# Add the elemnt at the index and shift the other elements 
list.insert(3,4000)

# Removes the value or the element form the list
# and only the first occurence
list.remove(6)
print(list)

# Pop removes the elemnt at that given index
list.pop(0)
print(list)

# SOrt 
list.sort()



people_list = ["eric", "adam", "jhon"]
print(people_list)
people_list[0]="ellen"
print(people_list[0])

#Slicing excluding the last element 
print(people_list[0:2])