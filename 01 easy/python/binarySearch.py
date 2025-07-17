# 704 https://leetcode.com/problems/binary-search/description/
# Attempts: 1

def binarySearch(nums: list[int], target: int) -> int:
    lowest = 0
    highest = len(nums) - 1
    
    while lowest <= highest:
        middle = (highest + lowest) // 2
        current = nums[middle]
        
        if current == target:
            return middle
        elif current > target:
            highest = middle - 1
        else:
            lowest = middle + 1
    
    return -1


### TEST CASES ###
print(binarySearch([-1, 0, 3, 5, 9, 12], 9))
print(binarySearch([-1, 0, 3, 5, 9, 12], 2))
print(binarySearch([-1, 0, 3, 5, 9, 12], 12))
print(binarySearch([-1, 0, 3, 5, 9, 12], -3))
