# 2300. Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
# Attempts:


import math

from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    potions.sort()
    result = []
    for i in spells:
        threshold = math.ceil(success / i)
        result.append(binary_search(potions, threshold))
    return result


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    middle = (right + left) // 2
    result = len(arr)

    while left <= right:
        curr = arr[middle]
        if target > curr:
            left = middle + 1
        else:
            right = middle - 1
            result = middle

        middle = (right + left) // 2

    return len(arr) - result


### TC Analysis

# sort(m) -> O(m log m)
# iterate n + binary search(potions) -> O(n log m)

### TEST CASES
print(successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
print(successfulPairs([3, 1, 2], [8, 5, 8], 16))
print(successfulPairs([15, 8, 19], [38, 36, 23], 328))
