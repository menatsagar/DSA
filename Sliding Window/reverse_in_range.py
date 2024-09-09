"""
Problem Description
Given an array A of N integers and also given two integers B and C. Reverse the elements of the array A within the given inclusive range [B, C].

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109
0 <= B <= C <= N - 1

Input Format
The first argument A is an array of integer.
The second and third arguments are integers B and C

Output Format
Return the array A after reversing in the given range.

Example Input
Input 1:

A = [1, 2, 3, 4]
B = 2
C = 3
Input 2:

A = [2, 5, 6]
B = 0
C = 2

Example Output
Output 1:

[1, 2, 4, 3]
Output 2:

[6, 5, 2]

Example Explanation
Explanation 1:

We reverse the subarray [3, 4].
Explanation 2:

We reverse the entire array [2, 5, 6].
"""

A = [1, 2, 3, 4]
B = 2
C = 3

x = [2, 5, 6]
y = 0
z = 2


class Solution:

    def reverse_in_range(self, arr, start, end):
        
        while start<end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp

            start+=1
            end-=1

        return arr
    

s = Solution()
p = s.reverse_in_range(A, B, C)
q= s.reverse_in_range(x, y,z)
print(p, q)


