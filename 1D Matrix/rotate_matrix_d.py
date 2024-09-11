"""
Problem Description
You are given a n x n 2D matrix A representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note: If you end up using an additional array, you will only receive partial score.



Problem Constraints
1 <= n <= 1000



Input Format
First argument is a 2D matrix A of integers



Output Format
Return the 2D rotated matrix.



Example Input
Input 1:

 [
    [1, 2],
    [3, 4]
 ]
Input 2:

 [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ]


Example Output
Output 1:

 [
    [3, 1],
    [4, 2]
 ]
Output 2:

 [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
 ]


Example Explanation
Explanation 1:

 After rotating the matrix by 90 degree:
 1 goes to 2, 2 goes to 4
 4 goes to 3, 3 goes to 1
Explanation 2:

 After rotating the matrix by 90 degree:
 1 goes to 3, 3 goes to 9
 2 goes to 6, 6 goes to 8
 9 goes to 7, 7 goes to 1
 8 goes to 4, 4 goes to 2



Expected Output
Enter your input as per the following guideline:
There are 1 lines in the input

Line 1 ( Corresponds to arg 1 ) : 2 D array. First 2 integers R, C are the number of rows and columns. Then R * C integers follow corresponding to the rowwise numbers in the 2D array
"""

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
         n = len(matrix)
         
         for row in range(n):
              col = row
              while col < n:
                    if row != col:
                       temp = matrix[row][col]
                       matrix[row][col] = matrix[col][row]
                       matrix[col][row] = temp    
                    col+=1

         for row in range(n):
              start = 0
              end = n-1
              while start<end:
                   temp = matrix[row][start]
                   matrix[row][start] = matrix[row][end]
                   matrix[row][end] = temp
                   start+=1
                   end-=1
         return matrix         

s=Solution()
A= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ]

p = s.rotate(A)
print(p)

