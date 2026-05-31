# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Attempts: 1


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    if root == None:
        return result

    queue = [root]
    while queue:
        curr_level = []
        next_level_nodes = []
        for node in queue:
            curr_level.append(node.val)
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)

        result.append(curr_level)
        queue = next_level_nodes

    return result
