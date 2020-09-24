"""

Given a lowercase alphabet string s, return a string with all the vowels of s in sorted order followed by all the consonants of s in sorted order.

Note: vowels are ["a", "e", "i", "o", "u"] and consonants are all other characters.

Constraints

Length of s ≤ 50000
Example 1
Input

s = "decalin"
Output

"aeicdln"
Explanation

Vowels are "eai" which when sorted is "aei"
Consonants are "dcln" which when sorted is "cdln"
Their concatenation is "aeicdln"

"""

class Solution:
    def solve(self, s):
        vowels = []
        consonants = []
        for i in range(0, len(s)):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                vowels.append(s[i])
            else:
                consonants.append(s[i])
        vowels.sort()
        consonants.sort()
        return "".join(vowels + consonants)