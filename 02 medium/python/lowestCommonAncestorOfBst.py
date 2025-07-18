# 235 https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# Attempts: 1

class TreeNode:
    def __init__(self, x, left=None, right=None) -> None:
        self.val = x
        self.left = left
        self.right = right

def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root.val == p.val or root.val == q.val:
        return root
    if root.val > p.val and root.val < q.val:
        return root
    if root.val < p.val and root.val > q.val:
        return root
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return lowestCommonAncestor(root.right, p, q)

