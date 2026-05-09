# LeetCode 9 - Palindrome Number

## Problem Description
The goal of this algorithm is to determine whether an integer (`x`) is a palindrome. An integer is a palindrome when it reads the same backward as forward (e.g., `121` is a palindrome, while `-121` is not due to the negative sign).

## Implementation and Logic
The solution focuses on simplicity and logical efficiency by leveraging Python's string manipulation capabilities:

1. **Negative Number Handling**: The algorithm first checks if the number is negative. Since a negative sign (`-`) at the beginning would end up at the end when reversed, negative integers are immediately identified as non-palindromic, returning `False`.
2. **String Conversion and Slicing**: The integer is converted into a string to enable sequence operations. Using Python's slicing notation `[::-1]`, the code creates a reversed copy of the string efficiently.
3. **Direct Comparison**: The original string is compared with the reversed version. Instead of using complex conditional branches, the function directly returns the result of this boolean comparison (`True` or `False`), ensuring clean and readable code.

## Execution Example
```python
sol = Solution()

# Example 
result1 = sol.isPalindrome(121)
# Expected output: True