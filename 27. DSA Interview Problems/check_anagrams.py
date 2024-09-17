# LeetCode - 242
"""
Problem Description
You are given two lowercase strings A and B each of length N. Return 1 if they are anagrams to each other and 0 if not.

Note : Two strings A and B are called anagrams to each other if A can be formed after rearranging the letters of B.


Problem Constraints
1 <= N <= 105
A and B are lowercase strings


Input Format
Both arguments A and B are a string.


Output Format
Return 1 if they are anagrams and 0 if not


Example Input
Input 1:
A = "cat"
B = "bat"
Input 2:
A = "secure"
B = "rescue"


Example Output
Output 1:
0
Output 2:
1
    

Example Explanation
For Input 1:
The words cannot be rearranged to form the same word. So, they are not anagrams.
For Input 2:
They are an anagram.
"""

from typing import List


class Solution:
    def check_anagrams(self, A, B):

        freq_a = {}
        if len(A) != len(B):
            return 0

        for char in A:
            if char not in freq_a:
                freq_a[char] = 0
            freq_a[char] += 1
        
        for char in B:
            if char not in freq_a:
                return 0

            if freq_a[char] > 1:
                freq_a[char]-=1
            else:
                del    freq_a[char]

        return 1
    
A = "secure"
B = "rescue"
    
s  =  Solution()
p = s.check_anagrams(A, B)
print(p)

