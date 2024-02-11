class MyClass:
    # Constructor
    def __init__(self, nums): #self pass in every method, like 'this' key word in outher languages
        # create member variables
        self.nums = nums # creating a member variables called nums and assigning it to the nums that were passed in as a parameter to the Constructor
        self.size = len(nums)
    
    #self key word required as parameters
    def getlength(self):
        return self.size
    
    #If call another member variable from a member variable
    def getDoubleLength(self):
        return 2 * self.getlength()    
    
myObj = MyClass([1, 2, 3])
print(myObj.getlength())  # This will print the length of the nums list, which is 3.
print(myObj.getDoubleLength()) # This will print double the length of the nums list, which is 6.
