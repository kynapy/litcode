# 216. Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/description/
# Attempts: 1


from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
    return combinationHelper(k, n, 1)


def combinationHelper(k: int, n: int, start: int) -> List[List[int]]:
    result = []
    if k == 1:
        for i in range(start, 10):
            if i == n:
                result.append([i])
        return result

    else:
        for i in range(start, 10):
            next = combinationHelper(k - 1, n - i, i + 1)
            for r in next:
                result.append(
                    [
                        i,
                    ]
                    + r
                )

    return result


### TEST CASES
print(combinationSum3(3, 7))
print(combinationSum3(3, 9))
print(combinationSum3(4, 1))
