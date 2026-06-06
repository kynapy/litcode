# 2336. Smallest Number in Infinite Set
# https://leetcode.com/problems/smallest-number-in-infinite-set/description/
# Attempts: 2

import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.hashset = set()
        self.heap = []
        self.counter = 1

    def popSmallest(self) -> int:
        if self.heap:
            result = heapq.heappop(self.heap)
            self.hashset.remove(result)
            return result
        else:
            result = self.counter
            self.counter += 1
            return result

    def addBack(self, num: int) -> None:
        if num < self.counter and num not in self.hashset:
            self.hashset.add(num)
            heapq.heappush(self.heap, num)


### TEST CASES
s = SmallestInfiniteSet()
print(s.popSmallest())
print(s.popSmallest())
s.addBack(3)
print(s.popSmallest())
s.addBack(2)
print(s.popSmallest())
print(s.popSmallest())
