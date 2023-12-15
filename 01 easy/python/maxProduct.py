class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = nums[0]
        second = nums[1]
        if first > second:
            highest = first
            secondHighest = second
        else:
            highest = second
            secondHighest = first
        for i in range(2, len(nums)):
            num = nums[i]
            if num > highest:
                secondHighest = highest
                highest = num
            elif num > secondHighest:
                secondHighest = num
        return (highest - 1) * (secondHighest - 1)