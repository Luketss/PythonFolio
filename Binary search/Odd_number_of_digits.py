"""
Given a list of positive integers nums, return the number of integers that have odd number of digits.

Example 1
Input

nums = [1, 800, 2, 10, 3]
Output

4
Explanation

[1, 800, 2, 3] have odd number of digits."""

class Solution:
    def solve(self, nums):
        
        odd_numbers = []
        
        for value in range(0, len(nums)):
            
            if len(str(nums[value])) % 2 != 0:
                odd_numbers.append(value)
            else:
                continue
        return len(odd_numbers)
