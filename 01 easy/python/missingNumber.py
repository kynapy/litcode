# 268. Missing Number

class Solution:
    def missingNumber(self, nums):
        listTotal = 0
        supposedTotal = 0
        for num in nums:
            listTotal += num
        for num in range(len(nums) + 1):
            supposedTotal += num
        return supposedTotal - listTotal

print(Solution().missingNumber([3,0,1]))
print(Solution().missingNumber([0,1]))
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))