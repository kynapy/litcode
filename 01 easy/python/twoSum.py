class Solution(object):
    def twoSum(self, nums, target):
        first, second = 0,0
        for i in range(len(nums)):
            secondTarget = target - nums[i]
            try:
                second = nums.index(secondTarget, i+1)
                first = i
            except:
                pass
        return [first, second]