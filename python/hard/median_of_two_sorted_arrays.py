# Problem: Median of Two Sorted Arrays
# Difficulty: Hard
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# Description:
# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log(m+n)).
#
# Approach (current - to be refactored):
# Concatenate both arrays using numpy, sort and calculate the median.
# This works but uses an external library and does not meet the expected
# O(log(m+n)) complexity. Needs to be refactored using binary search.
# Time: O((m+n) log(m+n)) | Space: O(m+n)
#
# TODO: Refactor using binary search to achieve O(log(m+n))

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = list(nums1) + list(nums2)
        nums.sort()
        n = len(nums)
        if n % 2 == 1:
            return float(nums[n // 2])
        return (nums[n // 2 - 1] + nums[n // 2]) / 2.0
