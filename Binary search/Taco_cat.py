"""
Given a string s, return whether it is a palindrome. A palindrome is when the word is the same forwards and backwards.

For example, "tacocat" is a palindrome.

Example 1
Input

s = "racecar"
Output

True
Example 2
Input

s = "evilolive"
Output

True
Example 3
Input

s = "palindrome"
Output

False
"""

class Solution:
    def solve(self, s):
        
        if s == s[::-1]:
            return True
        else:
            return False