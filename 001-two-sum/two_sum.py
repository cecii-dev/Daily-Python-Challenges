"""
LeetCode #1: Two Sum
Description: Find two distinct indices in a list where the sum of their values 
equals a predefined target.
"""

class Solution(object):
    def twoSum(self, nums: list[int], target: int):

        try:
            for i in range(len(nums)):
                expected_num = target - nums[i]
                if expected_num in nums and nums.index(expected_num) != i:
                    return [i,nums.index(expected_num)]
        except TypeError:
            raise TypeError("An error occurred: target and input numbers must be integers.")
        return []
            