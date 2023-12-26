# 108. Convert Sorted Array to Binary Search Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        middle = nums[len(nums) // 2]
        head = TreeNode(middle)
        self.createLeft(nums=nums[0:len(nums) // 2], head=head)
        self.createRight(nums=nums[len(nums) // 2 + 1:], head=head)
        return head

    def createLeft(self, nums, head):
        if nums:
            middle = nums[len(nums) // 2]
            curr = TreeNode(val=middle)
            head.left = curr
            self.createLeft(nums=nums[0:len(nums) // 2], head=curr)
            self.createRight(nums=nums[len(nums) // 2 + 1:], head=curr)
        else:
            return

    def createRight(self, nums, head):
        if nums:
            middle = nums[len(nums) // 2]
            curr = TreeNode(val=middle)
            head.right = curr
            self.createLeft(nums=nums[0:len(nums) // 2], head=curr)
            self.createRight(nums=nums[len(nums) // 2 + 1:], head=curr)
        else:
            return

Solution().sortedArrayToBST([1])