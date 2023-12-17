import re

class Solution:
    def isPalindrome(self, s):
        s = str.lower(s)
        s = re.sub(r'[\W_]+', '', s)
        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                return False
        return True   

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))
print(Solution().isPalindrome("ab_a"))
