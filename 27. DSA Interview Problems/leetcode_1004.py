"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        zeros = []
        max_ones = 0

        for i in range(n):
            if nums[i]== 0:
                zeros.append(i)

        if  len(zeros) <= k:
            return n

        for i in range(len(zeros)-k+1):
            curr_ones = 0
            prev_zero_index = zeros[i-1]
            
            if i!= 0 and i!= len(zeros)-k:
                curr_ones = zeros[i+k] - prev_zero_index -1   

            elif i==0:
                curr_ones = zeros[k]

            else :
                curr_ones = n - prev_zero_index -1                             
            
            max_ones = max(max_ones, curr_ones)
        
        return max_ones
    
nums = [1,1,1,0,0,0,1,1,1,1,0]
nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k2 = 3
k = 2

s = Solution()

p = s.longestOnes(nums=nums, k=k)
print(p)