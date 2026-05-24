# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
# Attempts:

from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    num_zeroes = 0
    curr_length = 0
    max_length = 0
    for i in range(len(nums)):
        curr_length += 1
        if nums[i] == 0:
            num_zeroes += 1

        while num_zeroes > k:
            if curr_length == 0:
                break
            else:
                if nums[i - curr_length + 1] == 0:
                    num_zeroes -= 1
                    curr_length -= 1
                else:
                    curr_length -= 1

        if curr_length > max_length:
            max_length = curr_length

    return max_length


def betterLongestOnes(nums: List[int], k: int) -> int:
    curr_length = 0
    curr_sum = 0
    max_length = 0
    for i in range(len(nums)):
        curr_length += 1
        curr_sum += nums[i]

        while curr_length - curr_sum > k:
            if curr_length == 0:
                break
            curr_sum -= nums[i - curr_length + 1]
            curr_length -= 1

        if curr_length > max_length:
            max_length = curr_length

    return max_length


# New implementation uses the sum instead, as the array is a binary array with 1s and 0s


### TEST CASES
print(betterLongestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(betterLongestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(betterLongestOnes([1, 1], 2))
print(betterLongestOnes([0], 0))
print(betterLongestOnes([0, 0, 0, 0], 0))
print(betterLongestOnes([0, 1, 1], 0))
