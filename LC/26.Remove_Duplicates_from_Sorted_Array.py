class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Initialize the first position on the u pointer
        u = 1
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is not equal to the previous element
            if nums[i] != nums[i - 1]:
                nums[u] = nums[i]
                u += 1  # Increment the u index itself, not nums[u]
        
        # Return the number of unique elements
        return u