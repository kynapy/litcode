# 134. Gas Station
# https://leetcode.com/problems/gas-station/description/
# Attempts: 3

from typing import List


def canCompleteCircult(gas: List[int], cost: List[int]) -> int:
    i = 0
    reached_end = False
    while i < len(gas) and not reached_end:
        if cost[i] > gas[i]:
            i += 1
            continue

        leftover = gas[i] - cost[i]
        curr_point = i
        while True:
            if curr_point + 1 >= len(gas):
                reached_end = True
            curr_point = (curr_point + 1) % len(gas)
            leftover = leftover + gas[curr_point] - cost[curr_point]

            if leftover < 0:
                i = curr_point + 1
                break

            if curr_point % len(gas) == i:
                return i

    return -1


def improvedCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    # Empty array
    if not gas:
        return -1

    length = len(gas)
    total_leftover = 0
    curr_leftover = 0
    start = 0

    for i in range(length):
        total_leftover += gas[i] - cost[i]
        curr_leftover += gas[i] - cost[i]
        if curr_leftover < 0:
            start = i + 1
            curr_leftover = 0
    if total_leftover < 0:
        return -1
    else:
        return start


### TEST CASES
print(canCompleteCircult([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(canCompleteCircult([2, 3, 4], [3, 4, 3]))
