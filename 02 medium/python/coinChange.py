# 322. Coin Change
# https://leetcode.com/problems/coin-change/description/
# Attempts: 3

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    memo = {}
    for i in range(amount + 1):
        memo[i] = amount + 1
    memo[0] = 0

    for curr_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= curr_amount:
                memo[curr_amount] = min(memo[curr_amount], memo[curr_amount - coin] + 1)

    if memo[amount] > amount:
        return -1
    else:
        return memo[amount]


### TEST CASES
print(coinChange([1, 2, 5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([1, 2147483647], 2))
print(coinChange([186, 419, 83, 408], 6249))
