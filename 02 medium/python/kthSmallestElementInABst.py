# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Attempts: 1

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    if root == None:
        return None

    stack = []
    stack.append(root)
    curr = root
    while curr.left:
        curr = curr.left
        stack.append(curr)

    pointer = stack[-1]
    while k > 0:
        pointer = stack.pop(-1)
        if pointer.right:
            right_child = pointer.right
            stack.append(right_child)
            while right_child.left:
                right_child = right_child.left
                stack.append(right_child)

        k -= 1

    return pointer.val
