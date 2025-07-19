# 110 https://leetcode.com/problems/balanced-binary-tree/description/
# Attempts: 1

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:
    balanceList = [True]
    if root:
        balanceChecker(root, balanceList)
    return balanceList[0]

def balanceChecker(root: TreeNode, balanceList: list[bool]) -> int:
    left_length, right_length = 0, 0
    if root.left:
        left_length = balanceChecker(root.left, balanceList) + 1
    if root.right:
        right_length = balanceChecker(root.right, balanceList) + 1

    if max(left_length, right_length) - min(left_length, right_length) > 1:
        balanceList[0] = False

    return max(left_length, right_length)
