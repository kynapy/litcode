# 1161. Maximum Level Sum of a Binary Tree
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
# Attempts: 1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxLevelSum(root: TreeNode) -> int:
    queue: list[TreeNode] = [root]
    max_sum = root.val
    current_level = 1
    max_level = current_level

    while queue:
        current_sum = 0
        new_queue = []

        for i in queue:
            current_sum += i.val
            if i.left:
                new_queue.append(i.left)
            if i.right:
                new_queue.append(i.right)

        if current_sum > max_sum:
            max_sum = current_sum
            max_level = current_level

        queue = new_queue
        current_level += 1

    return max_level


### TEST CASES
tree1 = TreeNode(1)
tree1.left = TreeNode(7)
tree1.right = TreeNode(0)
tree1.left.left = TreeNode(7)
tree1.left.right = TreeNode(-8)
print(maxLevelSum(tree1))
