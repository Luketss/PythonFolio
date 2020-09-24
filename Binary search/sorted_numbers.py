"""
Give a list of numbers nums, return the number of elements that are in the correct indices, if the list were to be sorted.

Example 1
Input

nums = [1, 7, 3, 4, 10]
Output

2
Explanation

Comparing nums and its sorted version we find that elements 1 and 10 are in their correct positions.

[1, 7, 3, 4, 10]
[1, 3, 4, 7, 10]
"""

class Solution:
    def solve(self, nums):
        new_list = sorted(nums)
        count = 0
        
        for x in range(0,len(nums)):
            
            if new_list[x] == nums[x]:
                count = count + 1
            else:
                continue
        return count
