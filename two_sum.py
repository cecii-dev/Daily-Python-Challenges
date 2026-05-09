"""
LeetCode #1: Two Sum
Description: Find two distinct indices in a list where the sum of their values 
equals a predefined target.
"""

class Solution(object):
    def twoSum(self, nums: list, target: int):

        for i in range(len(nums)):
            expected_num = target - nums[i]
            if expected_num in nums and expected_num != nums[i]:
                return [nums[i],expected_num]
            