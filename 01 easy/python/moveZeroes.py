# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums):
        zero_positions = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                zero_positions.append(i)
        for position in zero_positions:
            nums.pop(position)
        nums += [0] * len(zero_positions)
        return nums

print(Solution().moveZeroes([0,1,0,3,12]))
print(Solution().moveZeroes([0]))