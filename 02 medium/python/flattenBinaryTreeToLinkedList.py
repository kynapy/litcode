# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
# Attempts: 3

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: Optional[TreeNode]) -> None:
    if root == None:
        return
    if root.left:
        flatten(root.left)
    if root.right:
        flatten(root.right)

    if root.right and root.left:
        curr = root.left
        while curr.right:
            curr = curr.right
        curr.right = root.right
        root.right = root.left
        root.left = None
    if root.left:
        root.right = root.left
        root.left = None
