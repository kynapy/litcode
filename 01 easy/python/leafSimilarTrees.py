# 872. Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/description/
# Attempts: 1

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    root1Leaf = treeLeafArray(root1)
    root2Leaf = treeLeafArray(root2)

    if len(root1Leaf) != len(root2Leaf):
        return False
    for i in range(len(root1Leaf)):
        if root1Leaf[i] != root2Leaf[i]:
            return False
    return True


def treeLeafArray(root: TreeNode) -> list[int]:
    result = []
    stack = []
    stack.append(root)

    while stack:
        curr_node = stack.pop(-1)
        if not curr_node.left and not curr_node.right:
            result.append(curr_node.val)
        else:
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)

    return result


### TEST CASES
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root1.right = TreeNode(1)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

print(leafSimilar(root1, root2))
