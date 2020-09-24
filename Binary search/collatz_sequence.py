"""
Given a positve integer n, find the length of its Collatz sequence. Collatz sequence is generated sequentially where

n = n / 2 if n is even
n = 3 * n + 1 if n is odd
And the sequence ends if n = 1
Example 1
Input

n = 11
Output

15
Explanation

The Collatz sequence is: [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1] and its length is 15.
""""
class Solution:
    def solve(self, n):
        collatz = []

        while True:
            if n == 1:
                break
            else:
                if n % 2 == 0:
                    n = n/2
                    collatz.append(n)
                else:
                    n = 3 * n + 1
                    collatz.append(n)
        return len(collatz)+1