class Solution(object):
    def lengthOfLastWord(self, s):
        lastWord = ''
        wordFound = False
        if s:
            for i in range(1, len(s)+1):
                if s[-i] != " ":
                    wordFound = True
                    lastWord = s[-i] + lastWord
                else:
                    if wordFound:
                        break
        return len(lastWord)

# Test cases
test = Solution()
print(test.lengthOfLastWord('Hello World'))
print(test.lengthOfLastWord('    fly me   to the moon  '))
print(test.lengthOfLastWord('luffy is still joyboy'))