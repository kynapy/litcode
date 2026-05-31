# 15. 3Sum
# https://leetcode.com/problems/3sum/description/
# Attempts: 2


from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        curr_value = nums[i]

        if i != 0 and curr_value == nums[i - 1]:
            continue

        while left < right:
            left_value = nums[left]
            right_value = nums[right]

            curr_sum = left_value + right_value + curr_value
            if curr_sum == 0:
                result.append([curr_value, left_value, right_value])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif curr_sum > 0:
                right -= 1
            else:
                left += 1

    return result


### TEST CASES
print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 1, 1]))
print(threeSum([0, 0, 0]))
