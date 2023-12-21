# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1, nums2):
        result = []
        nums1.sort()
        nums2.sort()
        pointer1, pointer2 = 0, 0
        while True:
            if pointer1 >= len(nums1) or pointer2 >= len(nums2):
                break
            nums1_val = nums1[pointer1]
            nums2_val = nums2[pointer2]
            if nums1_val == nums2_val:
                result.append(nums1_val)
                pointer1 += 1
                pointer2 += 1
            elif nums1_val > nums2_val:
                pointer2 += 1
            else:
                pointer1 += 1
        return result

print(Solution().intersect([1,2,2,1], [2,2]))
print(Solution().intersect([4,9,5], [9,4,9,8,4]))