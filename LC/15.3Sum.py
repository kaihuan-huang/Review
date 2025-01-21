class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the triplets
        res = []
        
        # Sort the input list to facilitate two-pointer traversal
        nums.sort()

        # Iterate through the sorted list
        for i, a in enumerate(nums):
            # Skip duplicate values for the first element of the triplet
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Use two pointers: one starting right after `i` (l), and one at the end (r)
            l, r = i + 1, len(nums) - 1
            
            # Perform two-pointer traversal to find suitable triplets
            while l < r:
                # Calculate the sum of the current triplet
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    # If the sum is greater than 0, decrease the right pointer to reduce the sum
                    r -= 1
                elif threeSum < 0:
                    # If the sum is less than 0, increase the left pointer to increase the sum
                    l += 1
                else:
                    # If the sum equals 0, we found a valid triplet
                    res.append([a, nums[l], nums[r]])
                    
                    # Move the left pointer forward to look for other combinations
                    l += 1
                    
                    # Skip duplicate values for the second element of the triplet
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        # Return the list of triplets
        return res
