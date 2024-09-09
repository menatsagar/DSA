"""
Problem Description
Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes 
the sum of even-indexed and odd-indexed array elements equal.

Problem Constraints
1 <= N <= 105
-105 <= A[i] <= 105
Sum of all elements of A <= 109

Input Format
First argument contains an array A of integers of size N

Output Format
Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.

Example Input
Input 1:
A = [2, 1, 6, 4]
Input 2:

A = [1, 1, 1]


Example Output
Output 1:
1
Output 2:
3

Example Explanation
Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 
Therefore, the required output is 1. 
Explanation 2:

Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Therefore, the required output is 3.
"""


A = [2,1,3,4,2,4,2,1,34,5,2,1,4,2,4,3,1,3,2,1,3,34,4,5,6,3,2,1,8,9,6,9,0,2,3,8,6,3,4,4,2,2,1,8,5]

n = len(A)

odd_sum  = [0] * n
even_sum = [0] * n

odd_sum[0] = 0
even_sum[0] = A[0]                                                    #Insight:
                                                                      #We don't need to remove element for calculating if, we assume that current element
                                                                      # is removed then the next all indexes will be swpped
                                                                      #i.e.  odd index will become even and even index will become odd

for i in range(1, n):

    ele = A[i]

    if i%2 == 0:

        even_sum[i] = even_sum[i-1] + ele
        odd_sum[i] = odd_sum[i-1]

    else:
        
        even_sum[i] = even_sum[i-1]
        odd_sum[i] = odd_sum[i-1] + ele

count = 0

for i in range(n):

    if i !=0:

        odd = odd_sum[i-1] + even_sum[n-1]- even_sum[i]
        even = even_sum[i-1] + odd_sum[n-1] - odd_sum[i]

        
    else:
        odd =  even_sum[n-1]- even_sum[i]
        even =  odd_sum[n-1] - odd_sum[i]

    if odd==even:
            count+=1
            

print(count)