# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/description/
# Attempts: 1

from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    return combinationHelper(0, candidates, target)


def combinationHelper(start, candidates, target):
    result = []

    for i in range(start, len(candidates)):
        candidate = candidates[i]

        if target - candidate == 0:
            result.append([candidate])

        elif candidate > target:
            break

        else:
            new_results = combinationHelper(i, candidates, target - candidate)
            for r in new_results:
                result.append(
                    [
                        candidate,
                    ]
                    + r
                )

    return result


### TEST CASES
print(combinationSum([2, 3, 6, 7], 7))
print(combinationSum([2, 3, 5], 8))
print(combinationSum([2], 1))
