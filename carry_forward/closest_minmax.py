"""
Problem Description
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array

and at least one occurrence of the minimum value of the array.

Problem Constraints
1 <= |A| <= 2000

Input Format
First and only argument is vector A

Output Format
Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array

Example Input
Input 1:

A = [1, 3, 2]
Input 2:

A = [2, 6, 1, 6, 9]


Example Output
Output 1:

 2
Output 2:

 3

Example Explanation
Explanation 1:

 Take the 1st and 2nd elements as they are the minimum and maximum elements respectievly.
Explanation 2:

 Take the last 3 elements of the array.
"""

import math
max_ele = - math.inf
min_ele = math.inf

A = [1,2,3,2,4,3,5,7,4,3,2,5,7,9,87,6,3,2,12,34,5,3,12,34,4,6,3,2,4,3,2,7,5,6,4,23,4,5,6,5,3,2,4,5,56,4,3,1,3,5,6,7,6,4,2,2,23,2,1,2]



for i in range(len(A)):

    ele = A[i]

    if (ele > max_ele):
        max_ele = ele
    
    if ele < min_ele:
        min_ele = ele


start = -1
end = -1
min_subarray_length  = math.inf

for i  in range(len(A)):
    ele = A[i]
   

    if ele == min_ele:
        start = i
    
    if ele == max_ele:
        end = i
         

    if start != -1 and end != -1 :
        min_subarray_length = min(min_subarray_length, abs(end-start)+1)

    
print(min_subarray_length)    