# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# Attempts: 1


from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    minimal_length = len(nums) + 1
    curr_length = 0
    curr_sum = 0

    for i in range(len(nums)):
        curr_length += 1
        curr_sum += nums[i]

        while curr_sum >= target and curr_length > 0:
            if curr_length < minimal_length:
                minimal_length = curr_length

            curr_length -= 1
            curr_sum -= nums[i - curr_length]

    if minimal_length == len(nums) + 1:
        return 0
    return minimal_length


### TEST CASE
print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen(4, [1, 4, 4]))
