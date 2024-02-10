#Tuples are like array but immutable( initialze it with parentheses() instead of brackets[])
tup = (1, 2, 3)
print(tup)
print(tup[0], tup[-1])

#Can't modify 
# tup[0] = 5 'tuple' object does not support item assignment

# only use tuples as key for a hash map {} or hash set()
myMap = { (2, 3): 3}
print(myMap[2, 3])

# tuple is hashable key, but list cannot hashable
mySet = set()
mySet.add((1,2))
print((1,2) in mySet) 

# Lists cannot be keys 
# myMap[[4, 4]] = 5 TypeError: unhashable type: 'list'

