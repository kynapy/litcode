# 3010. Divide an Array Into Subarrays With Minimum Cost I
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description
# Attempts: 2

from typing import List


def minimumCost(nums: List[int]) -> int:
    total_cost = nums[0]  # First number always in cost
    current_firsts = (nums[1], nums[2])
    maximum_minimum = max(current_firsts)

    for i in range(3, len(nums)):
        current = nums[i]
        if current < maximum_minimum:
            if current_firsts[0] == maximum_minimum:
                current_firsts = (current, current_firsts[1])
            else:
                current_firsts = (current, current_firsts[0])
            maximum_minimum = max(current_firsts)

    for i in current_firsts:
        total_cost += i
    return total_cost


### TEST CASES
print(minimumCost([1, 2, 3, 12]))
print(minimumCost([5, 4, 3]))
print(minimumCost([10, 3, 1, 1]))
print(minimumCost([2, 16, 50, 35, 42, 11, 27, 24, 48, 4]))
