# TODO: Find better solution if it has

"""
Problem Description
You are given an integer array A. You have to find the second largest element/value in the array or 
report that no such element exists.

Problem Constraints
1 <= |A| <= 105
0 <= A[i] <= 109

Input Format
The first argument is an integer array A.

Output Format
Return the second largest element. If no such element exist then return -1.

Example Input

Input 1:
 A = [2, 1, 2] 

Input 2:
 A = [2]

Example Output

Output 1:
 1 
Output 2:
 -1 

Example Explanation

Explanation 1:
 First largest element = 2
 Second largest element = 1

Explanation 2:
 There is no second largest element in the array.
"""

A = [2, 1, 2]
import math

class Solution:

    def second_largest(self, arr):
        n = len(arr)

        first = -math.inf
        second = -math.inf
        has_second = False

        for i in range(n):    
            first = max(first, arr[i])

        for i in range(1,n):

            if  arr[i]< first and arr[i]>second:
                second = arr[i]
                has_second = True
        
        if has_second:
            return second 
        return -1

            
s = Solution()
p = s.second_largest([-1, -2, -3, -1, -3, -2])
print(p)