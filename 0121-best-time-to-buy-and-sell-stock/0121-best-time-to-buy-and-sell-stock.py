class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        left = 0
        right = left + 1
        while right <= len(prices) - 1:
            if prices[right] < prices[left]:
                left = right
                right = right + 1
            else: 
                max_profit = max(max_profit, prices[right] - prices[left])
                right = right + 1
        return max_profit