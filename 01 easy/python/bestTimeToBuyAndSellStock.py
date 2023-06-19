class Solution(object):
    def maxProfit(self, prices):
        biggestProfit = 0
        cheapest = prices[0]
        for price in prices:
            if price < cheapest:
                cheapest = price
            if price - cheapest > biggestProfit:
                biggestProfit = price - cheapest 
        return biggestProfit