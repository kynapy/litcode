class Solution(object):
    def removeDuplicates(self, nums):
        if nums:
            max = nums[-1]
            curr = nums[0]
            uniqueCount = set([])
            for i in range(len(nums)):
                if nums[i] in uniqueCount:
                    nums[i] = 'x'
                else:
                    uniqueCount.add(nums[i])
            while 'x' in nums:
                nums.remove('x')
            return len(uniqueCount)
        else:
            return 0

# Test cases
test = Solution()
print(test.removeDuplicates([1,1,2]))
print(test.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(test.removeDuplicates([]))