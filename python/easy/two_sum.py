# Problem: Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/
#
# Description:
# Given an array of integers nums and an integer target,
# return indices of the two numbers that add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# Approach:
# Hash map to store previously seen numbers and their indices.
# For each number, check if its complement (target - num) already exists.
# Time: O(n) | Space: O(n)

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
