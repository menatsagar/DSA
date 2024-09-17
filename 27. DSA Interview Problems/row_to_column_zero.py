"""
Problem Description
You are given a 2D integer matrix A, 
make all the elements in a row or column zero if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.



Problem Constraints
1 <= A.size() <= 103

1 <= A[i].size() <= 103

0 <= A[i][j] <= 103



Input Format
First argument is a 2D integer matrix A.



Output Format
Return a 2D matrix after doing required operations.



Example Input
Input 1:

[1,2,3,4]
[5,6,7,0]
[9,2,0,4]


Example Output
Output 1:

[1,2,0,0]
[0,0,0,0]
[0,0,0,0]


Example Explanation
Explanation 1:

A[2][4] = A[3][3] = 0, so make 2nd row, 3rd row, 3rd column and 4th column zero.
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0


        for c in range(cols):
            if matrix[0][c] ==0:
                for row in range(1,rows):
                    matrix[row][c] = 0

        for row in range(rows):
            
            if matrix[row][0] == 0:
                for col in range(1,cols):
                    matrix[row][col] = 0
        return matrix
       
        # return matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

s = Solution()
p = s.setZeroes(matrix)
print(p)