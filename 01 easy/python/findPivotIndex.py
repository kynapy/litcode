# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75
# Attempts: 5

from typing import List


def pivotIndex(nums: List[int]) -> int:
    # Edge cases
    if len(nums) == 1:
        return 0
    if sum(nums[1:]) == 0:
        return 0

    prefix_sum = []
    curr_sum = 0
    for i in nums:
        curr_sum += i
        prefix_sum.append(curr_sum)

    for i in range(1, len(nums) - 1):
        curr_num = nums[i]
        if curr_sum - curr_num - prefix_sum[i - 1] == prefix_sum[i - 1]:
            return i

    if curr_sum - nums[-1] == 0:
        return len(nums) - 1

    return -1


### TEST CASES
print(pivotIndex([1, 7, 3, 6, 5, 6]))
print(pivotIndex([1, 2, 3]))
print(pivotIndex([2, 1, -1]))
print(pivotIndex([-1, 1, -1]))
print(pivotIndex([-1, -1, -1, -1, -1, 0]))
print(pivotIndex([-1, -1, 1, 1, 0, 0]))
