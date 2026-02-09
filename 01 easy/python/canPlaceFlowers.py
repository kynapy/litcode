# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/description/
# Attempts: 2

from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    i = 0
    while i < len(flowerbed):
        curr = flowerbed[i]
        if curr == 0:
            # Last empty spot
            if i + 1 >= len(flowerbed):
                n -= 1
                i += 1
            
            # Next one empty
            elif flowerbed[i+1] != 1:
                i += 2
                n -= 1
            
            # Next one not empty, can skip next and the one after
            else:
                i += 3
        
        # Planted spot
        else:
            i += 2

    return n <= 0

### TEST CASES
print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1], 2))
print(canPlaceFlowers([1,0,0,0,0,1], 2))
print(canPlaceFlowers([1,0,0,0,0,0,1], 2))
print(canPlaceFlowers([1,0,0,0,1,0,0], 2))

