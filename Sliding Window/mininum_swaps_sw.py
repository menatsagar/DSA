"""
Problem Description

Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.



Problem Constraints

1 <= length of the array <= 100000
-109 <= A[i], B <= 109



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.



Output Format

Return the minimum number of swaps.



Example Input

Input 1:

 A = [1, 12, 10, 3, 14, 10, 5]
 B = 8
Input 2:

 A = [5, 17, 100, 11]
 B = 20


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 A = [1, 12, 10, 3, 14, 10, 5]
 After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
 After swapping  the first occurence of 10 and 5, A => [1, 3, 5, 12, 14, 10, 10].
 Now, all elements less than or equal to 8 are together.
Explanation 2:

 A = [5, 17, 100, 11]
 After swapping 100 and 11, A => [5, 17, 11, 100].
 Now, all elements less than or equal to 20 are together.
"""


"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
"""

import math

class Solution:

    def minimum_swaps(self, arr, target):
        
        n = len(arr)
        window_size = 0
        
        for i in range(n):
            if arr[i] <= target:
                window_size +=1
        
        swaps  = 0
        min_swaps = math.inf

        for i in range(window_size):
            if arr[i]>target:
                swaps+=1

        min_swaps = min(min_swaps, swaps)

        for i in range(1, n-window_size+1):
            new_ele = arr[i+window_size-1]
            prev_ele = arr[i-1]

            if new_ele > target:
                swaps +=1

            if prev_ele > target:
                swaps -= 1
            
            min_swaps = min(swaps, min_swaps)
        return min_swaps


A = [1,2,3,4,2,4,6,9,8,4,5,2,3,0,1,3,4,0,4,3,1,6,9,3,1,6,2]
B = 7

X = [5, 17, 100, 11]
Y = 20

s = Solution()
p = s.minimum_swaps(A, B)
q= s.minimum_swaps(X, Y)
print(p, q)
