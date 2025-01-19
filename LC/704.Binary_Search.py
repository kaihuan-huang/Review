class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # Initialize left and right pointers
        
        # Use a while loop to perform binary search
        while l <= r:
            m = (l + r) // 2  # Calculate the middle index
            
            # Check if the middle element is the target
            if nums[m] == target:
                return m  # Return the index if target is found
            
            # If the middle element is less than the target, search the right half
            elif nums[m] < target:
                l = m + 1  # Move the left pointer to the right
            
            # If the middle element is greater than the target, search the left half
            else:
                r = m - 1  # Move the right pointer to the left
        
        # If the target is not found, return -1
        return -1