# Median of Two Sorted Arrays - Hard


import numpy as np

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = np.concatenate((nums1, nums2))
        nums.sort()
        return np.median(nums)

solution = Solution()
result = solution.findMedianSortedArrays([1,3], [2,5])
print(result)