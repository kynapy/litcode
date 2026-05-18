# 547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/description/
# Attempts: 2


from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    connected = set()
    count = 0

    for i in range(len(isConnected)):
        if i in connected:
            continue
        else:
            queue = []
            queue.append(i)
            while queue:
                index = queue.pop(0)
                for j in range(len(isConnected[index])):
                    if j not in connected and isConnected[index][j] == 1:
                        connected.add(j)
                        queue.append(j)
            count += 1

    return count


### TEST CASES
print(findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
