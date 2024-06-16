# HeapSort
import heapq
nums = [1, 3, 5, 7, 9, 2]
heapq.heapify(nums)  #O(n)
while nums:
    heapq.heappop(nums) #O(logn)
    
# MergerSort (and most built-in sorting functions)

