# 77. Combinations
# https://leetcode.com/problems/combinations/description/
# Attempts: 1


from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    return combineHelper(n, k, 1)


def combineHelper(n: int, k: int, start):
    result = []
    if k == 1:
        for i in range(start, n + 1):
            result.append(
                [
                    i,
                ]
            )
        return result

    else:
        for i in range(start, n + 1):
            prev = combineHelper(n, k - 1, i + 1)
            for r in prev:
                result.append(
                    [
                        i,
                    ]
                    + r
                )
    return result


### TEST CASES
print(combine(4, 2))
print(combine(1, 1))
