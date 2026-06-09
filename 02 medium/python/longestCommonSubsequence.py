# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/description/
# Attempts: 2


def longestCommonSubsequence(text1: str, text2: str) -> int:
    result = []
    for _ in range(len(text1)):
        r = []
        for _ in range(len(text2)):
            r.append(-1)
        result.append(r)

    def dfs(index1, index2) -> int:
        if index1 == len(text1) or index2 == len(text2):
            return 0

        if result[index1][index2] != -1:
            return result[index1][index2]

        curr = 1 if text1[index1] == text2[index2] else 0
        end = None
        if curr:
            end = 1 + dfs(index1 + 1, index2 + 1)
        else:
            r1 = dfs(index1 + 1, index2)
            r2 = dfs(index1, index2 + 1)
            end = max(r1, r2)

        result[index1][index2] = end
        return end

    return dfs(0, 0)


### TEST CASES
print(longestCommonSubsequence("abcde", "ace"))
print(longestCommonSubsequence("abc", "abc"))
print(longestCommonSubsequence("abc", "def"))
print(longestCommonSubsequence("bsbininm", "jmjkbkjkv"))
