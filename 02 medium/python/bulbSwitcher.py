import math

class Solution:
    def bulbSwitch(self, n):
        return math.floor(math.sqrt(n))

print(Solution().bulbSwitch(1))
print(Solution().bulbSwitch(3))
print(Solution().bulbSwitch(99999))