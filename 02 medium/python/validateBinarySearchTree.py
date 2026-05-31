# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/description/
# Attempts: 1

import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    if root == None:
        return False

    left_valid = True
    right_valid = True
    if root.left:
        left_valid = isValidBstHelper(root.left, root.val - 1, -math.inf)
    if root.right:
        right_valid = isValidBstHelper(root.right, math.inf, root.val + 1)

    return left_valid and right_valid


def isValidBstHelper(root: TreeNode, max_val: int | float, min_val: int | float):
    if root.val > max_val or root.val < min_val:
        return False

    left_valid = True
    right_valid = True

    if root.left:
        left_valid = isValidBstHelper(root.left, root.val - 1, min_val)
    if root.right:
        right_valid = isValidBstHelper(root.right, max_val, root.val + 1)

    return left_valid and right_valid
