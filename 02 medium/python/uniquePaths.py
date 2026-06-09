# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/description/
# Attempts: 1


def uniquePaths(m: int, n: int) -> int:
    memo = {}
    return uniquePathHelper(m, n, memo)


def uniquePathHelper(m: int, n: int, memo: dict) -> int:
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 1 or n == 1:
        return 1

    result = 0
    result += uniquePathHelper(m - 1, n, memo)
    result += uniquePathHelper(m, n - 1, memo)

    memo[(m, n)] = result

    return result


### TEST CASES
print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
