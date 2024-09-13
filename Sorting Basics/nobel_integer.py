"""
Problem Description
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.



Problem Constraints
1 <= |A| <= 2*105
-108 <= A[i] <= 108


Input Format
First and only argument is an integer array A.



Output Format
Return 1 if any such integer p is present else, return -1.



Example Input
Input 1:

 A = [3, 2, 1, 3]
Input 2:


 A = [1, 1, 3, 3]


Example Output
Output 1:

 1
Output 2:

 -1

"""

class Solution:
    def nobel_interger(self, arr):
        arr = sorted(arr, reverse=True)
        n = len(arr)

        for i in range(n):

            if i==arr[i]:
                return 1
        return 0


s = Solution()
p = s.nobel_interger([3,2,1,3])
print(p)