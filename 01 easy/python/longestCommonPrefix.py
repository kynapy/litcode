class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs:
            longestPrefix = ''
            firstWord = strs[0]
            matched = True
            for i in range(len(firstWord)):
                for word in strs:
                    if len(word) >= i+1:
                        if word[i] != firstWord[i]:
                            matched = False
                    else:
                        matched = False
                        break
                if not matched:
                    break
                else:
                    longestPrefix += firstWord[i]
            return longestPrefix
        else:
            return ''

# Test Case
test = Solution()
print(test.longestCommonPrefix(['flower', 'flow', 'flower']))
print(test.longestCommonPrefix(['dog', 'racecar', 'car']))
print(test.longestCommonPrefix(['jessie', 'jessica', 'jesss']))