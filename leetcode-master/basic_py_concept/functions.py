
def ft(n, m):
    return n * m

print(ft(4, 5))

# Nested functions have access to outer variable 
# Really helpful in recursive problems
#outer funstions takes in a couple of parameters and declear some values, the inner funcition will have access to all of those variables by default, nice to keep the code concise

def outer(a, b):
    c = "c"
    def inner():
        return a + b + c
    return inner()
print(outer("a", "b"))

# Can modify object but not reassign values unless using nonlocal keyword
def double(arr, val):
    def helper():
        #can modifing the array
        for i, n in enumerate(arr):
            arr[i] *= 2
            # will only modify the value in the helper scope
            # val *= 2
            
            # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)
    
nums = [3, 4]
val = 3
double(nums, val)        
        
