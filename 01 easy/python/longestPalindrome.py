# 409 https://leetcode.com/problems/longest-palindrome/description/
# Attempts: 1

def longestPalindrome(s: str) -> int:
    word_dict = {}
    for letter in s:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1

    maximum_length = 0
    for letter in word_dict.keys():
        if word_dict[letter] >= 2:
            maximum_length += word_dict[letter] // 2 * 2
        word_dict[letter] = word_dict[letter] % 2
    
    for letter in word_dict.keys():
        if word_dict[letter] > 0:
            maximum_length += 1
            break

    return maximum_length

### TEST CASES ###
print(longestPalindrome("abccccdd"))
print(longestPalindrome("a"))
print(longestPalindrome("aaaaaaaaaaa"))
