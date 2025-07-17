# 226 https://leetcode.com/problems/invert-binary-tree/description/
# Attempts: 1

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left

def printBst(root: Optional[TreeNode]):
    if root:
        if root.left:
            printBst(root.left)
        print(root.val)
        if root.right:
            printBst(root.right)

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        if root.left:
            invertTree(root.left)
        if root.right:
            invertTree(root.right)

        temp = root.right
        root.right = root.left
        root.left = temp

    return root


### TEST CASES ###

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

printBst(root)
printBst(invertTree(root))
