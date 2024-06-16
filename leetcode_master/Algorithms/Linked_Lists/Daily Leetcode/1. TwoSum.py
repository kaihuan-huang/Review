def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {} #hashmap
    for i, n in enumerate(nums):
        comp = target - nums
        if comp in seen:
            return [seen[comp], i]
        seen[n] = i
    return []