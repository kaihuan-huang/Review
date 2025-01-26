class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Initialize pointers:
        # `i` points to the last valid element in nums1 (m - 1)
        # `j` points to the last element in nums2 (n - 1)
        # `p` points to the last position in nums1 (m + n - 1)
        i, j = m - 1, n - 1
        p = m + n - 1 # p = len(nums1) - 1 is equivalent to p = m + n - 1

        # Start merging from the end of nums1 to avoid overwriting elements
        while i >= 0 or j >= 0:
            # If all elements of nums2 have been merged, or nums1[i] > nums2[j]
            if j < 0 or (i >= 0 and nums1[i] > nums2[j]):
                # Place nums1[i] at position p
                nums1[p] = nums1[i]
                i -= 1  # Move the pointer `i` to the left
            else:
                # Place nums2[j] at position p
                nums1[p] = nums2[j]
                j -= 1  # Move the pointer `j` to the left
            p -= 1  # Move the position pointer `p` to the left
