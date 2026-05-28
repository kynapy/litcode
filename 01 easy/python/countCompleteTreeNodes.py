# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/description/
# Attempts: 1


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root: Optional[TreeNode]) -> int:
    max_depth = getMaxDepth(root)
    result = 0

    if max_depth == 0:
        return result

    result += 1
    if max_depth > 1:
        left_depth = getMaxDepth(root.left)
        right_depth = getMaxDepth(root.right)
        if left_depth == right_depth:
            result += getNodeCountOfFullBst(max_depth - 1) + countNodes(root.right)
        else:
            result += countNodes(root.left) + countNodes(root.right)

    return result


def getMaxDepth(root: Optional[TreeNode]) -> int:
    if root == None:
        return 0

    result = 1
    curr = root
    while curr.left:
        curr = curr.left
        result += 1
    return result


def getNodeCountOfFullBst(depth: int) -> int:
    result = 0
    for i in range(depth):
        result += 2**i
    return result
