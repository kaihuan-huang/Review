class Solutions:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() #check if element is in set
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


s = Solutions()
print(s.containsDuplicate([1, 2, 3, 1]))  # Output: True
print(s.containsDuplicate([1, 2, 3, 4]))  # Output: False
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True
