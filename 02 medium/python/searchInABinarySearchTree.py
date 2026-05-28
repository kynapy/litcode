# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
# Attempts: 1

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root == None:
        return None
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if curr.val == val:
            return curr
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return None
