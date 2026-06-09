# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/
# Attempts: 2

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    result = []
    curr = intervals[0]

    for start, end in intervals[1:]:
        if start <= curr[1]:
            if end > curr[1]:
                curr[1] = end
        else:
            result.append(curr)
            curr = [start, end]

    result.append(curr)
    return result


### TEST CASES
print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [4, 5]]))
print(merge([[4, 7], [1, 4]]))
