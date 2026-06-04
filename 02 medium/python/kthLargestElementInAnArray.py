# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Attempts: 1

from typing import List

import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    heap = []
    result = None
    for num in nums:
        heapq.heappush(heap, -num)

    for _ in range(k):
        result = heapq.heappop(heap) * -1

    return result


# Above solution works, but as we construct a heap of size n, we do the O(log n) insert n times.
# Thus, the time complexity is O(n log n), with a space complexity of O(n).
# However, we can use a heap of size k to reduce the time complexity to O(n log k), and space complexity of O(k).


def optimizedFindKthLargest(nums: List[int], k: int) -> int:
    heap = []

    for num in nums:
        if len(heap) >= k:
            if heap[0] < num:
                heapq.heappushpop(heap, num)
        else:
            heapq.heappush(heap, num)

    return heapq.heappop(heap)


### TEST CASES
print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

print(optimizedFindKthLargest([3, 2, 1, 5, 6, 4], 2))
print(optimizedFindKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
