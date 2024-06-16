'''Q: Find a non-empty subarray with the largest sum'''
def bruteForce(nums):
    maxSum = nums[0] 
    
    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum

'''Sliding Window technique base on two pointer:O(n)'''
'''Q: Return the left and right index of the max subarray sum, assuming there's exactly one result(no ties)'''
def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    l = 0
    for r in range(len(nums)):
        if curSum < 0:
            curSum = 0
            l = r
        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = l, r
    return[maxL, maxR]

