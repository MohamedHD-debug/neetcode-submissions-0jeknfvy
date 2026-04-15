class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        min_price = float('inf')
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            
            dp[i] = max(dp[i-1],prices[i]-min_price)

        return max(dp)
            