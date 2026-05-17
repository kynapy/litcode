# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/description/
# Attempts: 5

from typing import List


def findPeakElement(nums: List[int]) -> int:
    if len(nums) == 2:
        if nums[1] > nums[0]:
            return 1
        else:
            return 0

    low = 0
    high = len(nums) - 1

    while True:
        curr_index = low + (high - low) // 2
        if isPeak(nums, curr_index):
            return curr_index
        else:
            if nums[curr_index + 1] > nums[curr_index - 1]:
                low = curr_index + 1
            else:
                high = curr_index - 1


# Helper function
def isPeak(nums: List[int], index):
    if index == 0:
        if len(nums) == 1:
            return True
        else:
            return nums[0] > nums[1]
    elif index == len(nums) - 1:
        return nums[index] > nums[index - 1]
    else:
        return nums[index] > nums[index + 1] and nums[index] > nums[index - 1]


# Explanation

# O(log n) time: Cannot be linear search, need to use binary search
# An element that is not the peak has at least 1 neighbour larger than it.
# Moving in that direction, we are more likely to find more values that are the
# peak, or neighbours of the peak.


### TEST CASES
print(findPeakElement([1, 2, 3, 1]))
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(findPeakElement([2, 1]))
print(findPeakElement([1, 2, 3]))
