"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and
 all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""

from typing import List


class Solution:
  def diagonalSum(self, mat: list[list[int]]) -> int:
    n = len(mat)
    ans = 0

    for i in range(n):
      ans += mat[i][i]
      ans += mat[n - 1 - i][i]

    return ans if n % 2 == 0 else ans - mat[n // 2][n // 2]
    
A= [[1,2,3],
    
              [4,5,6],
              [7,8,9]]
B = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
C = [[5]]

s = Solution()
p = s.diagonalSum(B)
print(p)
        