class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() #check for duplicates in an array using a hash set.
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

# TC/SC = O(n)

# Test cases
print(containsDuplicate([1, 2, 3, 1]))  # Output: True
print(containsDuplicate([1, 2, 3, 4]))  # Output: False
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True