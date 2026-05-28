# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
# Attempts: 1

from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    min_cost_array = []
    min_cost_array.append(cost[0])
    min_cost_array.append(cost[1])

    for i in range(2, len(cost)):
        min_cost_array.append(
            cost[i] + min(min_cost_array[i - 1], min_cost_array[i - 2])
        )

    return min(min_cost_array[-1], min_cost_array[-2])


# Optimized for memory
def optimizedStairClimbing(cost: List[int]) -> int:
    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2, len(cost)):
        curr = cost[i] + min(prev2, prev1)
        prev1, prev2 = curr, prev1

    return min(prev1, prev2)


### TEST CASES
print(minCostClimbingStairs([10, 15, 20]))
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
