class Solution(object):
    def isValid(self, s):
        match = {'[':']', '{':'}', '(':')'}
        stack = []
        for char in s:
            if char in match.keys():
                stack.append(match[char])
            elif char in match.values():
                if len(stack) == 0:
                    return False
                else:
                    head = stack.pop()
                    if head != char:
                        return False
        if len(stack) != 0:
            return False
        return True