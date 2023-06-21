class Solution(object):
    def searchInsert(self, nums, target):
        front = 0
        back = len(nums)-1
        middle = 0
        while front < back:
            middle = back - front // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                back = middle - 1
            else:
                front = middle + 1
        if front == back:
            if nums[front] >= target:
                return front
            else:
                return front + 1
        return front



# Test cases
test = Solution()
print(test.searchInsert([1,3,5,6], 5))
print(test.searchInsert([1,3,5,6], 2))
print(test.searchInsert([1,3,5], 4))