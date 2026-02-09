# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/description/
# Attempts: 2


def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True

    subsequence = False
    s_index = 0
    t_index = 0
    while s_index < len(s) and t_index < len(t):
        if s[s_index] == t[t_index]:
            if s_index + 1 == len(s):
                subsequence = True
            s_index += 1
        t_index += 1
    return subsequence


### TEST CASES
print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
