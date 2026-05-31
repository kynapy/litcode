# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Attempts: 2


def lengthOfLongestSubstring(s: str) -> int:
    dictionary = {}
    longest = 0
    curr_length = 0

    for i in range(len(s)):
        curr_char = s[i]
        if curr_char not in dictionary or dictionary[curr_char] == 0:
            dictionary[curr_char] = 1
            curr_length += 1
            if curr_length > longest:
                longest = curr_length
        else:
            dictionary[curr_char] += 1
            curr_length += 1
            while dictionary[curr_char] > 1:
                removed_index = i - curr_length + 1
                dictionary[s[removed_index]] -= 1
                curr_length -= 1

    return longest


### TEST CASES
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("aab"))
