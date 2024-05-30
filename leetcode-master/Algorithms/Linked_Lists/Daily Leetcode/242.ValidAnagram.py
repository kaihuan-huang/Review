from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        
        for char in s:
            count_s[char] += 1
            
        for char in t:
            count_t[char] += 1
        
        return count_s == count_t