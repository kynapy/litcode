# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/description/
# Attempts:1

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    result = []
    pq: List[TreeNode] = []
    if root == None:
        return result
    pq.append(root)

    while pq:
        curr_pq = []
        for i in range(len(pq)):
            node = pq[i]
            if i == 0:
                result.append(node.val)
            if node.right:
                curr_pq.append(node.right)
            if node.left:
                curr_pq.append(node.left)
        pq = curr_pq

    return result
