# 1926. Nearest Exit from Entrance in Maze
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# Attempts: 3

from typing import List


# Memory Limit Exceeded
def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    pq = []
    pq.append(entrance)
    num_steps = 0

    while pq:
        curr_list = []
        for node in pq:
            if checkIfExit(maze, node, entrance):
                return num_steps
            surroundingNodes = getSurroundingNodes(maze, node)
            for surroundingNode in surroundingNodes:
                if maze[surroundingNode[0]][surroundingNode[1]] == ".":
                    curr_list.append(surroundingNode)
            maze[node[0]][node[1]] = "x"
        pq = curr_list
        num_steps += 1

    return -1


def getSurroundingNodes(maze: List[List[str]], point: List[int]) -> List[List[int]]:
    result = []

    if point[0] - 1 >= 0:
        result.append([point[0] - 1, point[1]])
    if point[1] - 1 >= 0:
        result.append([point[0], point[1] - 1])
    if point[0] + 1 < len(maze):
        result.append([point[0] + 1, point[1]])
    if point[1] + 1 < len(maze[0]):
        result.append([point[0], point[1] + 1])

    return result


def checkIfExit(maze: List[List[str]], point: List[int], entrance: List[int]) -> bool:
    if (
        point[0] == 0
        or point[1] == 0
        or point[0] == len(maze) - 1
        or point[1] == len(maze[0]) - 1
    ) and not (entrance[0] == point[0] and entrance[1] == point[1]):
        return True
    return False


# Optimized for memory
# 1. Remove double queue, measure distance in node list itself
# 2. Mark when with 'x' when enqueue, not dequeue


def nearestExitOptimized(maze: List[List[str]], entrance: List[int]) -> int:
    pq = []
    pq.append([entrance[0], entrance[1], 0])
    maze[entrance[0]][entrance[1]] = "x"

    while pq:
        curr_list = []
        for node in pq:
            if checkIfExit(maze, node, entrance):
                return node[2]
            surroundingNodes = getSurroundingNodes(maze, node)
            for surroundingNode in surroundingNodes:
                if maze[surroundingNode[0]][surroundingNode[1]] == ".":
                    curr_list.append(
                        [surroundingNode[0], surroundingNode[1], node[2] + 1]
                    )
                    maze[surroundingNode[0]][surroundingNode[1]] = "x"
        pq = curr_list

    return -1


### TEST CASES
print(nearestExit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]))
