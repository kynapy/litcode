# 94. Binary Tree Inorder Traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, input):
        self.stack.append(input)

    def pop(self):
        return self.stack.pop(len(self.stack) - 1)

    def notEmpty(self):
        if len(self.stack) != 0:
            return True
        return False

class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = Stack()
        if root != None:
            stack.push(root)
        while stack.notEmpty():
            curr = stack.pop()
            while curr.left:
                stack.push(curr)
                next = curr.left
                curr.left = None
                curr = next
            result.append(curr.val)
            if curr.right:
                stack.push(curr.right)
        return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(Solution().inorderTraversal(root))