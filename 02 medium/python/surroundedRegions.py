# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/description/
# Attempts: 2


from typing import List


def solve(board: List[List[str]]) -> None:
    visited = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            curr = board[i][j]
            if (i, j) not in visited and curr == "O":

                same_region = []
                to_be_searched = [(i, j)]
                touch_border = False

                while to_be_searched:
                    curr_node = to_be_searched.pop(0)
                    same_region.append(curr_node)
                    x = curr_node[0]
                    y = curr_node[1]
                    if x == 0 or x == len(board) - 1:
                        touch_border = True

                    if y == 0 or y == len(board[0]) - 1:
                        touch_border = True

                    surrounding_nodes = getNearbyRegion(board, curr_node, visited)
                    for node in surrounding_nodes:
                        to_be_searched.append(node)

                if not touch_border:
                    for node in same_region:
                        x = node[0]
                        y = node[1]
                        board[x][y] = "X"

            elif (i, j) not in visited:
                visited.add((i, j))


def getNearbyRegion(
    board: List[List[str]], area: tuple[int, int], visited: set
) -> List[tuple[int, int]]:
    result = []
    x = area[0]
    y = area[1]

    if x - 1 >= 0 and (x - 1, y) not in visited:
        if board[x - 1][y] == "O":
            result.append((x - 1, y))
        visited.add((x - 1, y))

    if x + 1 < len(board) and (x + 1, y) not in visited:
        if board[x + 1][y] == "O":
            result.append((x + 1, y))
        visited.add((x + 1, y))

    if y - 1 >= 0 and (x, y - 1) not in visited:
        if board[x][y - 1] == "O":
            result.append((x, y - 1))
        visited.add((x, y - 1))

    if y + 1 < len(board[0]) and (x, y + 1) not in visited:
        if board[x][y + 1] == "O":
            result.append((x, y + 1))
        visited.add((x, y + 1))

    return result


### TEST CASES
print(
    solve(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
    )
)

print(solve([["X"]]))
