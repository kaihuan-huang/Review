from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths of the strings are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Create default dictionaries for character counting
        count_s = defaultdict(int)
        count_t = defaultdict(int)

        # Count characters in string s
        for char in s:
            count_s[char] += 1

        # Count characters in string t
        for char in t:
            count_t[char] += 1

        # Check if both dictionaries are equal (i.e., if both strings have the same characters with the same frequency)
        return count_s == count_t