# Design a Dynamic Array( Resizable Array)
# Note: Python lists are dynamic arrays by default 
class DynamicArray:
    # O(n) n = capacity
    def __init__(self, capacity, init):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity
    
    # O(1)
    # Get value at i-th index 
    def get(self, i: int) -> int:
        return self.arr[i]
    
    # O(1)
    # Set value at i-th index
    def set_value(self, i: int, value: int) -> None:
        self.arr[i] = value
    
    # O(1) - Avg case/ Ammortized
    # Insert n in the last position of the array
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize() # 
        # insert the next empty position
        self.arr[self.size] = n
        self.size += 1
    
    # O(1)
    #Remove the last element in the array
    def popback(self) -> int:
        if self.length > 0:
            #soft delete the last element 
            self.length -= 1
        #return the popped element
        return self.arr[self.length]
    
    # O(n)
    def resize(self) -> None:
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity
        
        #Copy elements to new_arr
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
    
    # O(1)
    def getSize(self) -> int:
        return self.size
    # O(1)
    def getCapacity(self) -> int:
        return self.capacity

'''
Constructor (__init__): Initializes the array with a specified capacity.
get(index): Returns the element at the specified index.
set(index, element): Sets the element at the specified index to a new value.
pushback(element): Adds an element to the end of the array, resizing if necessary.
popback(): Removes and returns the last element of the array.
resize(): Doubles the array's capacity.
getSize(): Returns the number of elements in the array.
getCapacity(): Returns the current capacity of the array.
'''