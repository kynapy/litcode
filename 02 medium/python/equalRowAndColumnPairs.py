# 2352. Equal Row and Column Pairs
# https://leetcode.com/problems/equal-row-and-column-pairs/description/
# Attempts: 2

from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    encounted = {}
    for row in grid:
        row_item = ""
        for item in row:
            row_item += str(item) + ","
        if row_item in encounted:
            encounted[row_item] += 1
        else:
            encounted[row_item] = 1

    count = 0
    for i in range(len(grid[0])):
        column_item = ""
        for j in range(len(grid)):
            column_item += str(grid[j][i]) + ","
        if column_item in encounted:
            count += encounted[column_item]

    return count


### TEST CASES
print(equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
print(equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
