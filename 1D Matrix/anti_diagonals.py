"""
Problem Description
Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.


Problem Constraints
1<= N <= 1000
1<= A[i][j] <= 1e9


Input Format
Only argument is a 2D array A of size N * N.


Output Format
Return a 2D integer array of size (2 * N-1) * N, representing the anti-diagonals of input array A.
The vacant spaces in the grid should be assigned to 0.


Example Input
Input 1:
1 2 3
4 5 6
7 8 9
Input 2:

1 2
3 4


Example Output
Output 1:
1 0 0
2 4 0
3 5 7
6 8 0
9 0 0
Output 2:

1 0
2 3
4 0


Example Explanation
For input 1:
The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
The third anti diagonal of the matrix is [3, 5, 7 ], the rest spaces shoud be filled with 0 making the row as [3, 5, 7].
The fourth anti diagonal of the matrix is [6, 8 ], the rest spaces shoud be filled with 0 making the row as [6, 8, 0].
The fifth anti diagonal of the matrix is [9 ], the rest spaces shoud be filled with 0 making the row as [9, 0, 0].
For input 2:

The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
The third anti diagonal of the matrix is [3, 0, 0 ], the rest spaces shoud be filled with 0 making the row as [3, 0, 0].
"""

class Solution:
    def anti_diagonals(self, mat):
        rows = cols = len(mat)
        ans = [[0] * cols for _ in range(2*rows -1)]

        for col  in range(cols):
            row = 0
            temp  = [0] * cols
            temp[0] = mat[row][col]

            c = col
            r = row
            i = 0

            while c >= 0 and r < rows:
                temp[i] = mat[r][c]
                i+=1
                r+=1
                c-=1
                
                
            ans[col] = temp

        i = cols

        for row in range(1, rows):
            col = cols-1
            temp  = [0] * cols
            
            r = row
            c = col
            j = 0
            while c>=0 and r<rows:
                temp[j] = mat[r][c]
                r+=1
                c-=1
                j+=1
            ans[i] = temp
            i+=1
        return ans

A =[[1, 2, 3, 4],   
    [5, 6, 7, 8],   
    [9, 10,11,12],
    [13,14,15,16]]  

s = Solution()
p = s.anti_diagonals(A)
print(p)