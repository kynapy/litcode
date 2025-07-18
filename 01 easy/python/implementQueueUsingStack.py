# 232 https://leetcode.com/problems/implement-queue-using-stacks/description/
# Attempts: 1

class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, item) -> None:
        self.stack.append(item)

    def pop(self):
        return self.stack.pop(-1)

    def size(self) -> int:
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def isEmpty(self) -> bool:
        return self.size() == 0

class MyQueue:
    def __init__(self) -> None:
        self.queue = Stack()
        self.queue_reverser = Stack()

    def push(self, item) -> None:
        while not self.queue.isEmpty():
            self.queue_reverser.push(self.queue.pop())
        self.queue.push(item)
        while not self.queue_reverser.isEmpty():
            self.queue.push(self.queue_reverser.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.isEmpty()

### TESTS ###
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.empty())
print(queue.pop())
print(queue.empty())

