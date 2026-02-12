# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/description/
# Attempts: 1

from typing import List


def uniqueOccurrences(arr: List[int]) -> bool:
    occurrences = {}
    for n in arr:
        if n in occurrences:
            occurrences[n] += 1
        else:
            occurrences[n] = 1

    count = set()
    for occurrence in occurrences.values():
        if occurrence in count:
            return False
        else:
            count.add(occurrence)
    return True


### TEST CASES
print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print(uniqueOccurrences([1, 2]))
print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
