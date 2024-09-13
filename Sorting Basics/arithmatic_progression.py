"""
Problem Description
Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0.

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.



Problem Constraints
2 <= N <= 105

-109 <= A[i] <= 109



Input Format
The first and only argument is an integer array A of size N.



Output Format
Return 1 if the array can be rearranged to form an arithmetic progression, otherwise return 0.



Example Input
Input 1:

 A = [3, 5, 7]
Input 2:

 A = [2, 4, 1]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 We can reorder the elements as [1, 3, 5] or [5, 3, 1] with differences 2 and -2 respectively, between each consecutive elements.
Explanation 2:

 There is no way to reorder the elements to obtain an arithmetic progression.
"""

class Solution:
    
    def can_form_arithmatic_progression(self, arr):
        n = len(arr)

        if n<=2:
            return 1
        
        d = arr[1]-arr[0]

        for i in range(2, n):
            
            if arr[i]-arr[i-1] !=d:
                return 0
            
        return 1
    

s = Solution()
p = s.can_form_arithmatic_progression([3,5,7])
print(p)