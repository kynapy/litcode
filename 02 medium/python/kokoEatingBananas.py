# 875 https://leetcode.com/problems/koko-eating-bananas/description/
# Attempts: 3

import math

from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    largestPileSize = max(piles)
    minimumSpeed = 1
    return binarySearch(piles, minimumSpeed, largestPileSize, h)

def binarySearch(piles: List[int], lowest: int, highest: int, timeConstraint: int):
    if lowest >= highest:
        return lowest
    middle = (highest + lowest) // 2
    ableToFinish = finishEatingBananas(piles, middle, timeConstraint)
    if ableToFinish:
        return binarySearch(piles, lowest, middle, timeConstraint)
    else:
        return binarySearch(piles, middle + 1, highest, timeConstraint)
    

# Predicate function
def finishEatingBananas(piles: List[int], eatingSpeed: int, timeConstraint: int) -> bool:
    currentTime = 0
    for i in range(len(piles)): 
        pileSize = piles[i]
        pileTime = math.ceil(pileSize / eatingSpeed)

        currentTime += pileTime
        if currentTime > timeConstraint:
            return False
    return True

# print(finishEatingBananas([3, 6, 7, 11], 3, 8))

# TEST CASES
print(minEatingSpeed([3, 6, 7, 11], 8))
print(minEatingSpeed([30, 11, 23, 4, 20], 5))
print(minEatingSpeed([30, 11, 23, 4, 20], 6))
print(minEatingSpeed([3, 15], 6))
print(minEatingSpeed([312884470], 312884469))
print(minEatingSpeed([312884470], 968709470))
