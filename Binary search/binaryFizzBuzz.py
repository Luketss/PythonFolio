"""
Given an integer n, return a list of integers from 1 to n as strings except for multiples of 3 use 
“Fizz” instead of the integer and for the multiples of 5 use “Buzz”. For integers which are multiples 
of both 3 and 5 use “FizzBuzz”.

Example 1
Input

n = 15
Output

["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]"""

class Solution:
    def solve(self, n):
        elements = []
        for value in range(1,n+1):
            if value % 3 == 0 and value % 5 == 0:
                elements.append("FizzBuzz")
            elif value % 3 == 0:
                elements.append("Fizz")
            elif value % 5 == 0:
                elements.append("Buzz")
            else:
                elements.append(str(value))
        return elements