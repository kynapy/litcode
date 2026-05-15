# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/
# Attempts: 3

from typing import List


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        current_distance = right - left
        current_area = current_distance * min(height[left], height[right])
        if current_area > max_area:
            max_area = current_area

        if height[right] > height[left]:
            left += 1
        else:
            right -= 1

    return max_area


# Explanation
# Starting at both edges, for the 2 points, the capacity we get is the 
# distance between multiplied by the min_height(point_1, point_2). If we fixed
# the smallest point, there is no way to get more capacity than the current, as
# the width decreases, while there is no way to get a water height more than 
# the current


### TEST CASES
print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
print(maxArea([1,2,3,4]))
print(maxArea([1,2,3,1000,9]))
