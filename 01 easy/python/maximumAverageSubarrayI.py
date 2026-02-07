# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/description/
# Attempts: 1


from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    current_index = 1
    maximum_sum = sum(nums[0:k])
    current_sum = sum(nums[0:k])
    while current_index + k - 1 < len(nums):
        current_sum -= nums[current_index - 1]
        current_sum += nums[current_index + k - 1]

        if current_sum > maximum_sum:
            maximum_sum = current_sum

        current_index += 1

    return maximum_sum / k


### TEST CASES
print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(findMaxAverage([5], 1))
