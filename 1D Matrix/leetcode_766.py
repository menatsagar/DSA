"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:


Input: matrix = 
[
[1,2,3,4],
[5,1,2,3],
[9,5,1,2]
]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:
Input: matrix = 
[
[1,2],
[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99

"""

from typing import List


class Solution:
    """
    [
    [1,2,3,4],
    [5,1,2,3],
    [9,5,1,2]
    ]
    """
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        for col in range(cols-1, -1, -1):
            r = 0
            c = col
            temp = matrix[r][c]
            c+=1
            r+=1

            while r<rows and c<cols:
                if matrix[r][c] != temp:
                    return False
                c+=1
                r+=1
        
        for row in range(1, rows):
            c = 0
            r = row
            temp = matrix[r][c]
            c+=1
            r+=1
            while c<cols and r<rows:
                if matrix[r][c] != temp:
                    return False
                c+=1
                r+=1
                
        return True
    

A = [
    [1,2,3,4],
    [5,1,2,3],
    [9,6,1,2]
    ]
B = [
[1,2],
[2,2]]
s = Solution()
p = s.isToeplitzMatrix(A)
print(p)