
class Solution(object):
    def partitionLabels(self, s):
        # 1. Create a dictionary to record the last occurrence of each character
        # 1. 创建一个字典来记录每个字符最后出现的位置
        hm = {}
        for i, n in enumerate(s):
            hm[n] = i  # Store the last index where character 'n' appears in the string
                      # 将字符 'n' 最后出现的索引存储在字典中
        
        # 2. Initialize variables for partitioning the string
        # 2. 初始化用于分区的变量
        partitions = []  # This will store the sizes of each partition
                         # 用于存储每个分区的大小
        start = 0  # Start index of the current partition
                   # 当前分区的起始索引
        end = 0    # End index of the current partition
                   # 当前分区的结束索引
        
        # 3. Iterate through the string to determine partitions
        # 3. 遍历字符串以确定分区
        for i, n in enumerate(s):
            # Update the end index to the farthest last occurrence of characters seen so far
            # 将结束索引更新为目前看到的字符最远的最后出现位置
            end = max(end, hm[n])
            
            # When the current index matches the end index, we can complete the partition
            # 当当前索引等于结束索引时，完成当前分区
            if i == end:
                # Calculate the size of the current partition and add it to the list
                # 计算当前分区的大小并将其添加到列表中
                partitions.append(i - start + 1)
                # Move the start index to the next character to begin a new partition
                # 将起始索引移动到下一个字符，开始一个新的分区
                start = i + 1
        
        # 4. Return the list of partition sizes
        # 4. 返回分区大小的列表
        return partitions
```

### 要点 (Key Points):
1. **字典的作用 (Dictionary's Role)**: 
   - `hm` 记录了字符串中每个字符的最后出现位置。这样可以确保每个字符出现在其分区中最后一次之后不会出现在其他分区。
   - `hm` stores the last index where each character appears in the string, ensuring that a character won't appear in another partition once its last occurrence is past.

2. **分区的逻辑 (Partitioning Logic)**:
   - 遍历字符串时，不断更新 `end` 为当前字符在字符串中的最后出现位置。
   - 当当前索引等于 `end` 时，意味着当前分区可以完成，因为在 `start` 到 `end` 之间所有字符的最后一次出现都在这个范围内。
   - As we iterate through the string, `end` is updated to the farthest last occurrence of any character seen so far. When the current index `i` equals `end`, the partition is complete since all characters in the current partition appear fully within the range from `start` to `end`.

3. **计算分区大小 (Calculating Partition Sizes)**:
   - 每次完成分区时，将当前分区的大小 `i - start + 1` 计算并存入 `partitions` 列表中。
   - After completing a partition, the size of the partition (`i - start + 1`) is added to the `partitions` list.

4. **时间复杂度 (Time Complexity)**:
   - 该算法的时间复杂度为 **O(n)**，因为它只遍历字符串一次，同时更新分区信息。
   - The time complexity is **O(n)** since the string is traversed only once while updating partition information.

这个代码将字符串划分为最少的部分，确保每个部分中的字符不会出现在其他部分中。
