# Hashmap
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ps = 0
        hm = {0: -1}
        maxL = 0
        for i, n in enumerate(nums):
            ps += 1 if n == 1 else -1
            if ps in hm:
                maxL = max(maxL, i - hm[ps])
            else:
                hm[ps] = i
        return maxL
    
# Prefix sum
