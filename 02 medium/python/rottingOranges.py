# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/description/
# Attempts: 1


from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    rotten_oranges = []
    num_fresh = 0
    num_minutes = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                rotten_oranges.append((i, j))
            if grid[i][j] == 1:
                num_fresh += 1

    current_rotten = len(rotten_oranges)
    total_oranges = num_fresh + current_rotten
    while True:
        next_rotten = []
        for position in rotten_oranges:
            i = position[0]
            j = position[1]

            if i - 1 >= 0 and grid[i - 1][j] == 1:
                next_rotten.append((i - 1, j))
                grid[i - 1][j] = 2
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                next_rotten.append((i + 1, j))
                grid[i + 1][j] = 2
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                next_rotten.append((i, j - 1))
                grid[i][j - 1] = 2
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                next_rotten.append((i, j + 1))
                grid[i][j + 1] = 2

        if len(next_rotten) == 0:
            if total_oranges != current_rotten:
                return -1
            else:
                return num_minutes

        rotten_oranges = next_rotten
        current_rotten += len(next_rotten)
        num_minutes += 1


### TEST CASES
print(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(orangesRotting([[0, 2]]))
