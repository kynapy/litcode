class Solution(object):
    def containDuplicate(self, nums):
        initialSize = len(nums)
        newSet = set(nums)
        newSize = len(newSet)
        return (initialSize != newSize)