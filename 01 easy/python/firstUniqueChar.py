# First Unique Character in a String
class Solution:
    def firstUniqChar(self, s):
        d = {}
        for c in s:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1

print(Solution().firstUniqChar('leetcode'))
print(Solution().firstUniqChar('loveleetcode'))
print(Solution().firstUniqChar('aabb'))