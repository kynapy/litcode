from operator import xor

class Solution:
    def singleNumber(self, nums):
        curr = nums[0]
        for i in range(1, len(nums)):
            curr = curr ^ nums[i]
        return curr

print(Solution().singleNumber([2,2,1,1,5,7,5,8,7]))
print(Solution().singleNumber([1,2,1,2,4]))