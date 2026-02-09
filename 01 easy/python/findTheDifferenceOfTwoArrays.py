# 2215. Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
# Attempts: 1

from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    distinct_1 = set()
    distinct_2 = set()
    for i in nums1:
        if i not in distinct_1:
            distinct_1.add(i)
    for i in nums2:
        if i not in distinct_2:
            distinct_2.add(i)

    result_1 = set()
    result_2 = set()
    for i in nums1:
        if i not in distinct_2:
            result_1.add(i)
    for i in nums2:
        if i not in distinct_1:
            result_2.add(i)

    return [list(result_1), list(result_2)]


### TEST CASES
print(findDifference([1, 2, 3], [2, 4, 6]))
print(findDifference([1, 2, 3, 3], [1, 1, 2, 2]))
