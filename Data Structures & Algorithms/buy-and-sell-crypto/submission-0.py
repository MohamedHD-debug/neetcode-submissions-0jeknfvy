class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        for i in range(1,len(prices)):
            min_price = min(prices[:i])
            if min_price < prices[i] :
                dp[i] = max(dp[i-1],prices[i]-min_price)
            else :
                dp[i] = dp[i-1]

        return max(dp)
            