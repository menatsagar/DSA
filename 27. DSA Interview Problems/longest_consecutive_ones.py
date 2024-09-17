"""
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. 
Find and return the length of the longest consecutive 1’s that can be achieved.


Input Format

The only argument given is string A.
Output Format

Return the length of the longest consecutive 1’s that can be achieved.
Constraints

1 <= length of string <= 1000000
A contains only characters 0 and 1.
For Example

Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7
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
    
Input =[1,1,1,0,1,1,1,0,1]
Input2 =[1,1,1,0,0,0]


s = Solution()
p = s.max_ones(Input2)
print(p)
    