# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/
# Attempts: 2


def generateParenthesis(n: int):
    result = []

    def dfs(left, right, curr):
        if right > left or left > n or right > n:
            return
        elif left == right and left == n:
            result.append(curr)
        else:
            dfs(left + 1, right, curr + "(")
            dfs(left, right + 1, curr + ")")

    dfs(0, 0, "")
    return result


### TEST CASES
print(generateParenthesis(3))
print(generateParenthesis(4))
