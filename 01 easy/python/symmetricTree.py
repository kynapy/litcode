# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        if root.left == None and root.right:
            return False
        if root.right == None and root.left:
            return False
        if root.right == None and root.left == None:
            return True
        if root.left.val != root.right.val:
            return False
        prev_lst =[root.left]
        prev_rst = [root.right]
        stillRunning = True
        while stillRunning:
            stillRunning = False
            lst, rst = [], []
            for node in prev_lst:
                if node == None:
                    pass
                else:
                    if node.left or node.right:
                        stillRunning = True
                    lst.append(node.left)
                    lst.append(node.right)
            for node in prev_rst:
                if node == None:
                    pass
                else:
                    if node.left or node.right:
                        stillRunning = True
                    rst.append(node.left)
                    rst.append(node.right)
            if self.symmetricRow(lst, rst) == False:
                return False
            prev_lst = lst
            prev_rst = rst
        return True

    def symmetricRow(self, leftRow, rightRow):
        if len(leftRow) != len(rightRow):
            return False
        for i in range(len(leftRow)):
            left = leftRow[i]
            right = rightRow[-i-1]
            if left == None or right == None:
                if left != right:
                    return False
            else:
                if left.val != right.val:
                    return False
        return True

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(2)
head.left.left = TreeNode(3)
head.left.right = TreeNode(4)
head.right.left = TreeNode(4)
head.right.right = TreeNode(3)

print(Solution().isSymmetric(head))

head = TreeNode(1)
head.left = TreeNode(0)

print(Solution().isSymmetric(head))

