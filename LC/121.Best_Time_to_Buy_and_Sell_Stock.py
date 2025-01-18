class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left pointer = buy; right pointer = sell
        maxP = 0 #max profit

        while r < len(prices):
            # profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP