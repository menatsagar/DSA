#https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/ --- Leetcode 1423
"""
Problem Description
You are given an integer array A of size N.

You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.

Find and return the maximum possible sum of the B elements that were removed after the B operations.

NOTE: Suppose B = 3, and array A contains 10 elements, then you can:

Remove 3 elements from front and 0 elements from the back, OR
Remove 2 elements from front and 1 element from the back, OR
Remove 1 element from front and 2 elements from the back, OR
Remove 0 elements from front and 3 elements from the back.


Problem Constraints
1 <= N <= 105   

1 <= B <= N

-103 <= A[i] <= 103



Input Format    
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return an integer denoting the maximum possible sum of elements you removed.



Example Input
Input 1:

 A = [5, -2, 3 , 1, 2]
 B = 3
Input 2:

 A = [ 2, 3, -1, 4, 2, 1 ]
 B = 4


Example Output
Output 1:

 8
Output 2:

 9


Example Explanation
Explanation 1:

 Remove element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
Explanation 2:

 Remove the first element and the last 3 elements. So we get 2 + 4 + 2 + 1 = 9
"""



import math
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        A = [ 2, 3, -1, 4, 2, 1 ]
        """
        length = len(cardPoints)
        last_index = length-1


        prefix_sum = [0]* length
        prefix_sum[0] = cardPoints[0]

        for i in range(1, len(cardPoints)):
            prefix_sum[i] = prefix_sum[i-1] + cardPoints[i]

        suffix_sum = [0] * (length+1)
        suffix_sum[length] = 0
        suffix_sum[last_index] = cardPoints[last_index]
        
        for i in range(last_index-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + cardPoints[i]

        max_sum = - math.inf
        
        for i in range(k+1):
            if i==0:
                max_sum = max(max_sum, suffix_sum[length-k])
    
            else:
                max_sum = max(max_sum, (suffix_sum[length-k+i] + prefix_sum[i-1]))
        return max_sum

p = Solution()
q = Solution()
ans = p.maxScore([ 2, 3, -1, 4, 2, 1 ], 4)

ans2 = q.maxScore([96,90,41,82,39,74,64,50,30], 8)
print(ans, ans2)

