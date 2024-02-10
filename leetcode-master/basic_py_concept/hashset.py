# Hash set() cannot contain any duplicate 
mySet = set()
mySet.add(1)
mySet.add(8)

print(mySet)
print(len(mySet))

print( 1 in mySet)
print( 2 in mySet)

mySet.remove(1)
print(mySet)

# list to set
print(set([4, 5, 6]))
print([4, 5, 6])

# Set comprehension
mySet = { i for i in range(9) }
print(mySet)
