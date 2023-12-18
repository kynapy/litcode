class Solution:
    def merge(self, nums1, m, nums2, n):
        list1_last = m - 1
        list2_last = n -1
        for i in range(m+n-1,-1,-1):
            if list2_last == -1:
                break
            elif list1_last == -1:
                nums1[i] = nums2[list2_last]
                list2_last -= 1
            else:
                if nums1[list1_last] <= nums2[list2_last]:
                    nums1[i] = nums2[list2_last]
                    list2_last -= 1
                else:
                    nums1[i] = nums1[list1_last]
                    list1_last -= 1
        return nums1

print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(Solution().merge([2,5,6,0,0,0], 3, [1,2,3], 3))
print(Solution().merge([1], 1, [], 0))
print(Solution().merge([0], 0, [1], 1))