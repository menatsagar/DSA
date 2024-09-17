"""
Given an array of 1's and 0's, find the maximum number of
consecutive 1's that can be obtained by SWAPPING at most one
0 with 1(already present in the string).
Input: [1, 0, 1, 1, 0, 1]
Output: 5
"""

class Solution:
    def max_ones(self, nums):

        n = len(nums)
        zeros = []
        max_ones = 0

        for i in range(n):
            if nums[i] == 0:
                zeros.append(i)

        if len(zeros) == 0:
            return n

        if len(zeros) == 1:
            return n-1
        
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
    
Input =[1, 0, 1, 1, 0, 1]

s = Solution()
p = s.max_ones(Input)
print(p)
    
