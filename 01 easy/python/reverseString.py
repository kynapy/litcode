class Solution:
    def reverseString(self, s):
        swap = ''
        for i in range(len(s) // 2):
            swap = s[i]
            s[i] = s[-i-1]
            s[-i-1] = swap
        return s

print(Solution().reverseString(['h', 'e', 'l', 'l', 'o']))
print(Solution().reverseString(['H', 'a', 'n', 'n', 'a', 'h']))