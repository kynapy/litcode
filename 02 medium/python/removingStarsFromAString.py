# 2390. Removing Stars From a String
# https://leetcode.com/problems/removing-stars-from-a-string/description/
# Attempts: 1


def removeStars(s: str) -> str:
    stack = []
    result = ""

    for i in s:
        if i == "*":
            stack.pop(-1)
        else:
            stack.append(i)

    for i in stack:
        result += i

    return result


### TEST CASES
print(removeStars("leet**cod*e"))
print(removeStars("erase*****"))
