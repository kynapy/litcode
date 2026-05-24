# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
# Attempts: 1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int:
    maxValue = root.val
    return recursiveSearch(root, int(maxValue))


def recursiveSearch(node: TreeNode, maxValue: int) -> int:
    if node.val > maxValue:
        maxValue = node.val

    left = 0
    right = 0

    if node.left:
        left += recursiveSearch(node.left, maxValue)
    if node.right:
        right += recursiveSearch(node.right, maxValue)

    if node.val >= maxValue:
        return 1 + left + right
    else:
        return 0 + left + right


### TEST CASES
t = TreeNode(3)
t.left = TreeNode(1)
t.right = TreeNode(4)
t.left.left = TreeNode(3)
t.right.left = TreeNode(1)
t.right.right = TreeNode(5)
print(goodNodes(t))
