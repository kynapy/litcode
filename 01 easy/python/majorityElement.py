# 169. Majority Element

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

print(Solution().majorityElement([3,2,3]))
print(Solution().majorityElement([2,2,1,1,1,2,2]))