# 198. House Robber
# https://leetcode.com/problems/house-robber/description/
# Attempts: 1


from typing import List


def rob(nums: List[int]) -> int:
    prev1 = 0
    prev2 = 0
    for num in nums:
        curr = max(prev2 + num, prev1)
        prev2 = prev1
        prev1 = curr

    return max(prev1, prev2)


### TEST CASES
print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))
