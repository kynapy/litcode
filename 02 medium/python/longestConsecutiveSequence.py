# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/
# Attempts: 1


from typing import List


def longestConsecutive(nums: List[int]) -> int:
    hashset = set()
    highest = 0

    for i in nums:
        hashset.add(i)

    for i in nums:
        if i in hashset:
            count = 1
            left = i - 1
            right = i + 1

            while left in hashset or right in hashset:
                if left in hashset:
                    hashset.remove(left)
                    left -= 1
                    count += 1
                if right in hashset:
                    hashset.remove(right)
                    right += 1
                    count += 1

            if count > highest:
                highest = count

    return highest


def optimizedLongestConsecutive(nums: List[int]) -> int:
    hashset = set()
    highest = 0

    for num in nums:
        hashset.add(num)

    for num in hashset:
        if num - 1 not in hashset:
            count = 1
            curr = num
            while curr + 1 in hashset:
                curr += 1
                count += 1

            if count > highest:
                highest = count

    return highest


### TEST CASES
print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longestConsecutive([1, 0, 1, 2]))
