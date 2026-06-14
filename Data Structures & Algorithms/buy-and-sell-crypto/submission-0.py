class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minTillNow = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if minTillNow > prices[i]:
                minTillNow = prices[i]
                continue
            maxProfit = max(maxProfit, prices[i] - minTillNow)
        
        return maxProfit
            