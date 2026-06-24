# 112. Path Sum
# https://leetcode.com/problems/path-sum/description/
# Attempts: 1


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if root == None:
        return False

    def dfs(root: TreeNode, currentSum: int):
        curr = root.val
        if root.left:
            l = dfs(root.left, currentSum + curr)
            if l:
                return True
        if root.right:
            r = dfs(root.right, currentSum + curr)
            if r:
                return True

        if root.left == None and root.right == None and curr + currentSum == targetSum:
            return True
        else:
            return False

    return dfs(root, 0)
