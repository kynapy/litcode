# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/description/
# Attempts: 1


from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    result = 0
    last_end = float("-inf")

    for start, end in intervals:
        if start < last_end:
            result += 1
        else:
            last_end = end

    return result


### TEST CASES
print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
print(eraseOverlapIntervals([[1, 2], [2, 3]]))
