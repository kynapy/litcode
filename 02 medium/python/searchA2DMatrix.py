# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/
# Attempts: 2


from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    min_index = 0
    max_index = len(matrix) - 1
    middle = (min_index + max_index) // 2

    while min_index < max_index:
        value = matrix[middle][-1]
        if value == target:
            return True
        elif value > target:
            max_index = middle
        else:
            min_index = middle + 1
        middle = (min_index + max_index) // 2

    return binarySearch(matrix[middle], target)


def binarySearch(array: List[int], target: int) -> bool:
    min_index = 0
    max_index = len(array) - 1

    while min_index <= max_index:
        middle = (min_index + max_index) // 2
        value = array[middle]
        if value == target:
            return True
        elif value > target:
            max_index = middle - 1
        else:
            min_index = middle + 1
        middle = (min_index + max_index) // 2

    return False


### TEST CASES
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(searchMatrix([[1]], 1))
