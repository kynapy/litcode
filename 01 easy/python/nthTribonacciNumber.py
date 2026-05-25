# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/description/
# Attempts: 1

from typing import List


# Recursive version of DP
def tribonacci(n: int) -> int:
    store = [0, 1, 1]
    if n > 2:
        store += [None] * (n - 2)
    return recursive_dp(n, store)


def recursive_dp(n: int, store: List):
    if store[n] != None:
        return store[n]
    else:
        result = (
            recursive_dp(n - 1, store)
            + recursive_dp(n - 2, store)
            + recursive_dp(n - 3, store)
        )
        store[n] = result
        return result


# Bottom up version of DP
def bottom_up_dp(n: int):
    store = [0, 1, 1]
    for i in range(3, n + 1):
        store.append(store[i - 1] + store[i - 2] + store[i - 3])
    return store[n]
