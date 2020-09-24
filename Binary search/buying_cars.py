"""
Given a list of integers prices representing prices of cars for sale, and a budget k, return the maximum number of cars you can buy.

Constraints

Length of prices ≤ 10000
Example 1
Input

prices = [90, 30, 20, 40, 90]
k = 95
Output

3
Explanation

We can buy the cars with prices 30, 20, and 40.

Example 2
Input

prices = [60, 90, 55, 75]
k = 50
Output

0
Explanation

We cannot afford any of these cars."""

class Solution:
    def solve(self, prices, k):
        count = 0
        prices.sort()
        
        for values in prices:
            
            if k >= values:
                count += 1
                k -= values
        return count        
