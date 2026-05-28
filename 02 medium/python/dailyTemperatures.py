# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/
# Attempts: 1


from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    result = [0] * len(temperatures)

    for i in range(len(temperatures)):
        temperature = temperatures[i]

        if len(stack) > 0:
            while stack and temperature > stack[-1][0]:
                curr = stack.pop(-1)
                result[curr[1]] = i - curr[1]
        stack.append((temperature, i))

    while stack:
        curr = stack.pop(-1)
        result[curr[1]] = 0

    return result


### TEST CASES
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(dailyTemperatures([30, 40, 50, 60]))
print(dailyTemperatures([30, 60, 90]))
