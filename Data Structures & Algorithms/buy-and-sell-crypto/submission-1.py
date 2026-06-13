class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0

        i = 0
        j = 1

        while j < n:
            if prices[i] < prices[j]:
                profit = max(profit, prices[j] - prices[i])
            else: 
                i = j
            j += 1
        
        return profit