'''Q: GIven an array, return true if there are two elements within a window of size k that are equal'''
'''1. Check if array contains a pair of duplicate values where the 2 duplicates are no further than k position from eachother 
i.e. arr[i] == arr[j] and abs(i - j) <= k). O(n * k)
'''

def closeDuplicatesBruteForce(nums, k):
    for l in range(len(nums)):
        for r in range( l + 1, min(len(nums), L + k)):
            if nums[l] == nums[r]:
                return True
    return False

 '''Optimized using HashSet(). O(n)'''
def closeDuplicates(nums, k):
    window = set() # Current window of size <= k
    l = 0
    for r in range(len(nums)):
        if r - l + 1 > k:
            window.remove(nums[l])
            l += 1
        if nums[r] in window:
            return True
        window.add(nums[r])
        
    return False

'''Q: Find the length of the longest subarray, with the same value in each position'''
# Find the length of longest subarray with the same value in each position: O(n)
def longestSubarray(nums):
    len = 0
    l = 0
    
    for r in range(len(nums)):
        if nums[l] != nums[r]:
            l = r
        len = max(len, r - l + 1)
    return len

'''Q: Find the minimun length subarray, where the sum is greater than or equal to the target. Assume all vlaues are positive'''
# O(n)
def shortestSubarray(nums, target):
    l, w_sum = 0, 0 #w_sum = window sum
    len = float("inf")
    
    for r in range(len(nums)):
        w_sum += nums[r]
        while w_sum >= target:
            len = min(r - l + 1, len)
            w_sum -= nums[l]
            l += 1
        
    return 0 if len == float("inf") else len
