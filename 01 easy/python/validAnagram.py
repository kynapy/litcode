# 242. Valid Anagram

class Solution:
    def isAnagram(self, s, t):
        log = {}
        for c in s:
            if c in log.keys():
                log[c] += 1
            else:
                log[c] = 1
        for c in t:
            if c in log.keys():
                log[c] -=1
            else:
                return False
        for value in log.values():
            if value != 0:
                return False
        return True

print(Solution().isAnagram('anagram', 'nagaram'))
print(Solution().isAnagram('rat', 'car'))