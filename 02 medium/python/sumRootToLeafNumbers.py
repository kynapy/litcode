# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
# Attempts: 1

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumNumbers(root: Optional[TreeNode]) -> int:
    return sumHelper(root, 0)


def sumHelper(root: Optional[TreeNode], amount: int) -> int:
    result = 0
    if root.left:
        result += sumHelper(root.left, amount * 10 + root.val)
    if root.right:
        result += sumHelper(root.right, amount * 10 + root.val)
    if not root.left and not root.right:
        result += amount * 10 + root.val

    return result
