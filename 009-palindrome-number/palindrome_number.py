"""
LeetCode #9: Palindrome Number
Description: Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.
"""

class Solution(object):
    def isPalindrome(self, x:int):

        if x < 0: # Negative number can't be a palindrome
            return False
        else:
            x = str(x)
            result = x[::-1]
            if result == x:
                return True
            else:
                return False