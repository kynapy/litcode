# 200 https://leetcode.com/problems/number-of-islands/description/
# Attempts: 3

from typing import List

def get_surroundings(current_position, grid):
    left, right, up, down = 0, 0, 0, 0
    if current_position[1] > 0:
        left = (current_position[0], current_position[1] - 1)
    if current_position[1] < len(grid[0]) - 1:
        right = (current_position[0], current_position[1] + 1)
    if current_position[0] > 0:
        up = (current_position[0] - 1, current_position[1])
    if current_position[0] < len(grid) - 1:
        down = (current_position[0] + 1, current_position[1])
    return left, right, up, down

def bfs_land(touched: set, grid: list[list[str]], current_position: tuple[int, int]):
    queue = []
    queue.append(current_position)

    while queue:
        current_pos = queue.pop(0)
        current_value = grid[current_pos[0]][current_pos[1]]
        if current_value == '1':
            left, right, up, down = get_surroundings(current_pos, grid)
            if left and left not in touched:
                queue.append(left)
                touched.add(left)
            if right and right not in touched:
                queue.append(right)
                touched.add(right)
            if up and up not in touched:
                queue.append(up)
                touched.add(up)
            if down and down not in touched:
                queue.append(down)
                touched.add(down)
        touched.add(current_pos)

def numberOfIslands(grid: List[List[str]]) -> int:
        touched = set()
        num_islands = 0

        for i in range(len(grid)):
            inner_list = grid[i]
            for j in range(len(inner_list)):
                current_position = (i, j)
                if current_position in touched:
                    continue
                else:
                    current_item = inner_list[j]
                    if current_item == '1':
                        bfs_land(touched, grid, current_position)
                        num_islands += 1
                    touched.add(current_position)
        return num_islands

