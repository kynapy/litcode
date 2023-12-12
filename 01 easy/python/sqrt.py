class Solution:
    def mySqrt(self, x: int) -> int:
        limit = x * 3
        for i in range(1, limit):
            if (i * i) > x:
                return i - 1
        return 0