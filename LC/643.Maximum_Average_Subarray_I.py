class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the initial sum of the first k elements
        cur = sum(nums[:k])
        res = cur

        # Slide the window through the array
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i - k] # Slide the window
            res = max(res, cur)
        
        # Return the maximum average
        return res / k
    