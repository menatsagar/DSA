"""
Given an array of 1's and 0's, you are allowed to replace only one
0 with 1. Find the maximum number of consecutive 1's that can
be obtained after making the replacement.
Input = [1, 1, 0, 1, 1, 0, 1, 1]
Output = 5
"""

class Solution:

    def max_ones(self, arr):
        n = len(arr)
        zeros = []
        max_ones = 0

        for i in range(n):
            if arr[i]== 0:
                zeros.append(i)

        if len(zeros)== 0 or len(zeros)==1:
            return n

        for i in range(len(zeros)):
            curr_ones = 0
            prev_zero_index = zeros[i-1]
            

            if i==0:
                curr_ones = zeros[i+1]

            elif i==len(zeros)-1:
                curr_ones = n - prev_zero_index -1
            else:
                curr_ones = zeros[i+1] - prev_zero_index -1                
            
            max_ones = max(max_ones, curr_ones)
        
        return max_ones 


        

Input = [1, 1, 0, 1, 1, 0, 1, 1]
s = Solution()
p = s.max_ones(Input)
print(p)

