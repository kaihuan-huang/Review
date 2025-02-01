class Solution(object):
    def frequencySort(self, s):
        # Step 1: Create a hashmap (dictionary) to count the frequency of each character
        hm = {}
        for n in s:
            if n in hm:
                hm[n] += 1  # If the character is already in the hashmap, increment its count by 1
            else:
                hm[n] = 1  # If the character is not in the hashmap, add it with an initial count of 1 
        
        # Step 2: Create buckets to group characters by their frequency
        # Each index in the 'buckets' list represents a frequency
        # The list at each index will store all characters that have that frequency
        buckets = [[] for _ in range(len(s) + 1)]
        
        # Step 3: Populate the buckets with characters based on their frequency
        for n, freq in hm.items():
            buckets[freq].append(n)  # Place the character in the bucket corresponding to its frequency
        
        # Step 4: Build the result string by collecting characters from the buckets
        top_k = []
        # Iterate over the buckets in reverse order (from highest frequency to lowest)
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                top_k.append(n * i)  # Append the character i times to the result list
                # The multiplication n * i repeats the character 'n' for 'i' times

        # Step 5: Join the list of strings into a single strin\g and return it
        return ''.join(top_k)
        
        """
        :type s: str
        :rtype: str
        """
