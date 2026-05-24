# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# Attempts: 1

from typing import List


def maxProfit(prices: List[int]) -> int:
    profit = 0
    prev_price = prices[0]
    for price in prices:
        if price > prev_price:
            profit += price - prev_price
        prev_price = price

    return profit


### TEST CASE
print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 2, 3, 4, 5]))
print(maxProfit([7, 6, 4, 3, 1]))
