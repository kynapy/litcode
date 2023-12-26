# 104. Maximum Depth of Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        result = 0
        if root == None:
            return result
        nodes = [root]
        while nodes:
            nodes_copy = nodes.copy()
            nodes.clear()
            for node in nodes_copy:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result += 1
        return result

head = TreeNode(val=3)
head.left = TreeNode(val=9)
head.right = TreeNode(val=20)
head.right.left = TreeNode(val=15)
head.right.right = TreeNode(val=7)

print(Solution().maxDepth(head))