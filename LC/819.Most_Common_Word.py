import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        # 1. Normalize the paragraph by converting to lowercase and replacing punctuations with spaces
        # 1. 通过将段落转换为小写并替换标点符号为单词间隔，标准化段落
        # re.findall(r'\w+', ...) extracts all words (alphanumeric characters) from the paragraph
        # re.findall(r'\w+', ...) 从段落中提取所有单词（由字母和数字组成的字符）
        words = re.findall(r'\w+', paragraph.lower())

        # 2. Create a set of banned words for quick lookup
        # 2. 将禁用单词列表转换为集合，便于快速查找
        banned_set = set(banned)

        # 3. Count the frequency of each word excluding the banned ones
        # 3. 统计未被禁用的单词的出现频率
        # The generator expression filters out words that are in the banned set
        # 生成器表达式过滤掉出现在禁用列表中的单词
        word_counts = Counter(word for word in words if word not in banned_set)

        # 4. Return the most common word
        # 4. 返回最常见的单词
        # word_counts.most_common(1) returns the most frequent word as a tuple (word, count)
        # word_counts.most_common(1) 返回最频繁的单词，格式为 (单词, 次数)
        return word_counts.most_common(1)[0][0]  # [0][0] extracts just the word
                                                # [0][0] 提取单词
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
