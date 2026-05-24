# 1679. Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/
# Attempts: 1

from typing import List


def maxOperations(nums: List[int], k: int) -> int:
    complements = {}
    result = 0
    for num in nums:
        complement = k - num
        if complement in complements and complements[complement] > 0:
            complements[complement] -= 1
            result += 1
        else:
            if num in complements:
                complements[num] += 1
            else:
                complements[num] = 1

    return result


### TEST CASES
print(maxOperations([1, 2, 3, 4], 5))
print(maxOperations([3, 1, 3, 4, 3], 5))
