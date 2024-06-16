# Array in python: Dynamic array be used as Stacks
arr = [2, 3, 4]
arr.append([5, 6])
print(arr)

arr.pop()
print(arr)

# array: we can insert the value 7 to the index 1; inserting to an array cost TC: O(n)
arr.insert(1, 7)
print(arr)

# we can reassign the value at index [0]...: these operations are constant time TC: O(n)
arr[0] = 0
arr[3] = 0
print(arr)

# Initialze arr of size n with default value of 5 
n = 10
arr = [5] * n # [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
print(arr)
print(len(arr))

# In python -1 is the last value 
arr = [4, 5, 6]
print(arr[-1])
print(arr[-2])

# Sublists (AKA slicing) ****+ imprtant
arr = [2, 3, 4, 5]
print(arr[1: 3]) # get the value form index 1 to the index 3, last index is not included

# But no out of bounds error, which can print all the values from index 0 to the end of the array
print(arr[0:10])

# Unpacking ** important, the variables on the left needed match with the the right
a, b, c = [4, 5, 6]
print(b, a, c)

# Loop
nums = [3, 4, 5, 6]
# Using Index
for i in range(len(nums)):
    print(nums[i])
    
#without Inex
for n in nums:
    print(n)

# with Index and value
for i, n in enumerate(nums):
    print(i, n)
    
# loop through multiple arrays simultaneously with unpacking using helper() function called zip: zip() will take both arrays combine in to an array of pairs, and unpack those pair of values
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for n1, n2 in zip(nums1, nums2):
    print("n1",n1, "n2", n2) 
    
# reverse()
nums.reverse()
print("reverse", nums)

# sorting
arr.sort()
print("sorted", arr)

arr = ["bob", "alice", "jane", "doe"] # default sorting by alphabetical order
arr.sort()
print(arr)

#Costom: sort by length of the string: pasing a lambda function: 
arr.sort(key=lambda x: len(x)) #key=lambda means a function without a name, and we going to take every single value from the array call it x, len(x) is the key used to sort the string: each string is going to map to it's string, and then sort their string base on their length; by default ascending order
print(arr) #['bob', 'doe', 'jane', 'alice']

# another intialize the array: List comprehension
arr = [i+i for i in range(5)]
print(arr)

# 2-D List
arr = [[3] * 4 for i in range (10)]
print(arr) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print(arr[3][2]) #第三行第二列

