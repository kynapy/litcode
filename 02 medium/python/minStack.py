# 155. Min Stack
# https://leetcode.com/problems/min-stack/description/
# Attempts: 2


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.min_stack) == 0 or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        result = self.stack.pop(-1)
        if result == self.min_stack[-1]:
            self.min_stack.pop(-1)
        return result

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


### TEST CASES
minstack = MinStack()
minstack.push(-2)
minstack.push(0)
minstack.push(-3)
print(minstack.getMin())
minstack.pop()
print(minstack.top())
print(minstack.getMin())
