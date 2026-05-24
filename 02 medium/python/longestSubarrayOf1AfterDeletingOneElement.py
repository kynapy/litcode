# 1493. Longest Subarray of 1's After Deleting One Element
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
# Attempts: 1


from typing import List


def longestSubarray(nums: List[int]) -> int:
    longest_subarray = 0
    num_zeroes = 0
    current_length = 0

    for i in range(len(nums)):
        current_length += 1
        if nums[i] == 0:
            num_zeroes += 1

        while num_zeroes > 1:
            if nums[i - current_length + 1] == 0:
                num_zeroes -= 1
            current_length -= 1

        if current_length - 1 > longest_subarray:
            longest_subarray = current_length - 1

    return longest_subarray


### TEST CASES
print(longestSubarray([1, 1, 0, 1]))
print(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(longestSubarray([1, 1, 1]))
