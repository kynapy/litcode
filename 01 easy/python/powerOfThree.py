# 326. Power Of Three
class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n >= 3:
            if n % 3 == 0:
                n = n / 3
            else:
                return False
        if n != 0:
            return False
        else:
            return True

print(Solution().isPowerOfThree(27))
print(Solution().isPowerOfThree(0))
print(Solution().isPowerOfThree(-1))