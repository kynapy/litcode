# 909. Snakes and Ladders
# https://leetcode.com/problems/snakes-and-ladders/description/
# Attempts: 2

from collections import deque
from typing import List


def snakesAndLadders(board: List[List[int]]) -> int:
    visited = set()
    visited.add(1)
    queue = deque()
    queue.append(1)
    result = 0
    n = len(board)
    n_squared = n**2

    def getMatrixPosition(num: int) -> tuple[int, int]:
        idx = num - 1
        row = n - 1 - idx // n
        col = idx % n if (n - 1 - row) % 2 == 0 else n - 1 - (idx % n)
        return row, col

    while queue:
        next_queue = deque()
        while queue:
            curr = queue.popleft()
            if curr == n_squared:
                return result

            for i in range(1, 7):
                landing = curr + i
                if landing <= n_squared:
                    row, col = getMatrixPosition(curr + i)
                    target = board[row][col]
                    if target != -1:
                        landing = target

                    if landing not in visited:
                        next_queue.append(landing)
                        visited.add(landing)

        result += 1
        queue = next_queue

    return -1


### TEST CASES
print(
    snakesAndLadders(
        [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ]
    )
)


print(
    snakesAndLadders(
        [
            [-1, -1, -1, 46, 47, -1, -1, -1],
            [51, -1, -1, 63, -1, 31, 21, -1],
            [-1, -1, 26, -1, -1, 38, -1, -1],
            [-1, -1, 11, -1, 14, 23, 56, 57],
            [11, -1, -1, -1, 49, 36, -1, 48],
            [-1, -1, -1, 33, 56, -1, 57, 21],
            [-1, -1, -1, -1, -1, -1, 2, -1],
            [-1, -1, -1, 8, 3, -1, 6, 56],
        ]
    )
)
