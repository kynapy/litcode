# 171. Excel Sheet Column Number
class Solution:
    def titleNumber(self, columnTitle):
        result = ord(columnTitle[0]) - 64
        for i in range(1, len(columnTitle)):
            c = columnTitle[i]
            result *= 26
            result += ord(c) - 64
        return result

print(Solution().titleNumber("A"))
print(Solution().titleNumber("AB"))
print(Solution().titleNumber("ZY"))
print(Solution().titleNumber("FXSHRXW"))