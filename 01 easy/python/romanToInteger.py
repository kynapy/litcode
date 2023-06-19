class Solution(object):
    def romanToInt(self, s):
        reference = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(s)):
            if s[i] == 'I' and i+1 < len(s):
                if s[i+1] == "V" or s[i+1] == "X":
                    result -= 1
                else:
                    result += 1
            elif s[i] == "X" and i+1 < len(s):
                if s[i+1] == "L" or s[i+1] == "C":
                    result -= 10
                else:
                    result += 10
            elif s[i] == "C" and i+1 < len(s):
                if s[i+1] == "D" or s[i+1] == "M":
                    result -= 100
                else:
                    result += 100
            else:
                result += reference[s[i]]
        return result

# Test cases
test = Solution()
print(test.romanToInt('III'))
print(test.romanToInt('LVIII'))
print(test.romanToInt('MCMXCIV'))