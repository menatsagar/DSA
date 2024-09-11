"""
Problem Constraints
1 <= A.size() <= 103

1 <= A[i].size() <= 103

1 <= A[i][j] <= 103



Input Format
First argument A is a 2D array of integers.(2D matrix).



Output Format
Return an array containing row-wise sums of original matrix.



Example Input
Input 1:

[1,2,3,4]
[5,6,7,8]
[9,2,3,4]


Example Output
Output 1:

[10,26,18]


Example Explanation
Explanation 1

Row 1 = 1+2+3+4 = 10
Row 2 = 5+6+7+8 = 26
Row 3 = 9+2+3+4 = 18
"""

class Solution:
    def row_sum(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])
        row_sum = [0]*rows

        for row in range(rows):
            
            col = 0
            temp = 0

            while col<cols:
                temp+=matrix[row][col]
                col+=1

            row_sum[row] = temp
        return row_sum

A = [[1,2,3,4],
[5,6,7,8],
[9,2,3,4]
]

s = Solution()
p = s.row_sum(A)
print(p)