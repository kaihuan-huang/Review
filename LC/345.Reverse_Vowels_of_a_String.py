class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert the input string to a list to allow in-place modification
        s = list(s)

        # Initialize two pointers: one starting from the left, one from the right
        l, r = 0, len(s) - 1

        # Define a set of vowels for quick lookup (both lowercase and uppercase)
        vowels = set("aeiouAEIOU")

        # Use a while loop to process the string until the pointers meet or cross
        while l < r:
            # Move the left pointer `l` forward until it points to a vowel
            # Skip over all non-vowel characters
            while l < r and s[l] not in vowels:
                l += 1

            # Move the right pointer `r` backward until it points to a vowel
            # Skip over all non-vowel characters
            while l < r and s[r] not in vowels:
                r -= 1

            # Swap the vowels at the `l` and `r` pointers
            s[l], s[r] = s[r], s[l]

            # Move both pointers inward after the swap
            l += 1
            r -= 1

        # Convert the list back to a string and return the result
        return ''.join(s)