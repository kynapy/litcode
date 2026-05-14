# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/
# Attempts: 1

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    left_to_right = []
    right_to_left = []

    curr_product = 1
    for i in range(len(nums)):
        curr_product *= nums[i]
        left_to_right.append(curr_product)

    curr_product = 1
    for i in range(1, len(nums) + 1):
        curr_product *= nums[-i]
        right_to_left = [
            curr_product,
        ] + right_to_left

    answer = []
    for i in range(len(nums)):
        if i == 0:
            answer.append(right_to_left[1])
        elif i == len(nums) - 1:
            answer.append(left_to_right[-2])
        else:
            answer.append(left_to_right[i - 1] * right_to_left[i + 1])

    return answer


# O(1) space constraint
def productInPlace(nums: List[int]) -> List[int]:
    answer = []

    curr_product = 1
    for i in range(len(nums)):
        curr_product *= nums[i]
        answer.append(curr_product)

    curr_product = 1
    for i in range(1, len(nums) + 1):
        curr_product *= nums[-i]
        nums[-i] = curr_product

    last_value = answer[-2]

    for i in range(1, len(nums) + 1):
        if i == len(nums):
            answer[-i] = nums[1]
        elif i == 1:
            answer[-i] = last_value
        else:
            answer[-i] = answer[-i - 1] * nums[-i + 1]

    return answer


### TEST CASES
print(productInPlace([1, 2, 3, 4]))
print(productInPlace([-1, 1, 0, -3, 3]))
