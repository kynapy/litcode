class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)

# Test cases
test = Solution()
print(test.strStr('sadbutsad' ,'but'))
print(test.strStr('leetcode', 'leeto'))