# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
# Attempts: 1


from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    if not points:
        return 0

    arrows = 1
    points.sort(key=lambda x: x[1])
    last_end = points[0][1]

    for start, end in points[1:]:
        if start > last_end:
            last_end = end
            arrows += 1

    return arrows


### TEST CASES
print(findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
