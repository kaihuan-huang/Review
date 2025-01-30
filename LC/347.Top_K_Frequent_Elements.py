class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Build a frequency map
        freq_map = {}
        for n in nums: 
            freq_map[n] = freq_map.get(n, 0) + 1
        
        #Step 2: Initialize empty buckets[],  
        buckets = [[] for _ in range(len(nums) +1 )]

        #Step 3: Fill the buckets
        for n, freq in freq_map.items():
            buckets[freq].append(n)

        #Step4: Collect top k frequent elements
        top_k = []
        for i in range(len(buckets) -1, 0, -1):
            for n in buckets[i]:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k

# Test the function
print(topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(topKFrequent([1], 1))            # Output: [1]
