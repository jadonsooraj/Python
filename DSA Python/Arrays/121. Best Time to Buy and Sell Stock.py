# M1: 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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


# M2: keep a track of a min_price, check for profit at each ele in one raversal
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            profit = prices[i] - min_price

            if profit > max_profit:
                max_profit = profit
            if prices[i] < min_price:
                min_price = prices[i]
        
        return max_profit