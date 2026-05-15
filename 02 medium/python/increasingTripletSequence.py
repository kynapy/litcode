# 334. Increasing Triplet Sequence
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
# Attempts: 3

from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    smallest = nums[0]
    middle = None

    for i in nums:
        if middle == None:
            if i <= smallest:
                smallest = i
            else:
                middle = i
        else:
            if i <= smallest: 
                smallest = i
            elif i <= middle:
                middle = i
            else: 
                return True

    return False

# Greedy solution

# For every number from left to right, if the number is smaller than the 
# smallest in the previous numbers, then any number bigger than those numbers 
# would be bigger than the current number

# If there is a bigger number than the previous smaller numbers, then we have 
# a middle number, and any future number bigger than the middle number creates a triplet.

# If the future number is smaller than the smallest, then we can keep it as 
# the smallest while tracking the current middle. Anything bigger than the
# current middle generates a triplet, and smaller than the current middle, we
# assign it as the middle, as anything smaller than the new middle will be 
# smaller than the old middle.

### TEST CASES
print(increasingTriplet([1,2,3,4,5]))
print(increasingTriplet([5,4,3,2,1]))
print(increasingTriplet([2,1,5,0,4,6]))
print(increasingTriplet([2,4]))


