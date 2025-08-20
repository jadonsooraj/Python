class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l,r = 0,0 # l=buy, r=sell
        maxProfit = 0
        while r < len(prices):
            # profitable?
            profit = prices[r] - prices[l]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                l=r
            r+=1
        return maxProfit