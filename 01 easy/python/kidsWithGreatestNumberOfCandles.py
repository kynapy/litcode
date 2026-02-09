# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
# Attempts: 1

from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    result = []
    amount_to_beat = 0
    for i in candies:
        if i > amount_to_beat:
            amount_to_beat = i

    for i in candies:
        if i + extraCandies >= amount_to_beat:
            result += [
                True,
            ]
        else:
            result += [
                False,
            ]

    return result


### TEST CASES
print(kidsWithCandies([2, 3, 5, 1, 3], 3))
print(kidsWithCandies([4, 2, 1, 1, 2], 1))
print(kidsWithCandies([12, 1, 12], 10))
