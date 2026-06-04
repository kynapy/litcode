# 46. Permutations
# https://leetcode.com/problems/permutations/description/
# Attempts: 1


from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    if len(nums) == 1:
        return [[nums[0]]]
    else:
        result = []
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i + 1 :]
            new_result = permute(new_nums)
            curr = nums[i]
            for r in new_result:
                result.append(
                    [
                        curr,
                    ]
                    + r
                )

        return result


### TEST CASES
print(permute([1, 2, 3]))
print(permute([0, 1]))
print(permute([1]))
