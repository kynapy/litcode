# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# Attempts: 3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    stack = []
    curr = root
    target = None

    while True:
        if curr == p:
            target = q
            break
        if curr == q:
            target = p
            break

        if curr.left:
            stack.append(curr)
            curr = curr.left
        elif curr.right:
            stack.append(curr)
            curr = curr.right
        else:
            while stack:
                parent = stack.pop(-1)
                if parent.right:
                    curr = parent.right
                    break

    # Check if it is it's own LCA
    children = [curr]
    while children:
        scan = children.pop(0)
        if scan == target:
            return curr
        if scan.left:
            children.append(scan.left)
        if scan.right:
            children.append(scan.right)

    while stack:
        potential_lca = stack.pop(-1)

        queue = [potential_lca]
        while queue:
            pointer = queue.pop(0)
            if pointer == target:
                return potential_lca
            if pointer.left:
                queue.append(pointer.left)
            if pointer.right:
                queue.append(pointer.right)
