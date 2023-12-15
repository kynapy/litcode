class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else: # iterative fibonacci
            first = 1
            second = 2
            while n > 2:
                next = first + second
                first = second
                second = next
                n -= 1
            return next

print(Solution().climbStairs(44))