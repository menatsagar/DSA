#https://leetcode.com/problems/maximum-subarray/description/

"""
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""



import math


class Solution:
    def maxSubArray(self, nums) -> int:

        

        length = len(nums)

        all_positive = True
        all_negative = True
        negative_max = -math.inf
        
        for i in range(length):
            
            if nums[i]<0:
                all_positive = False
                break
        
        for i in range(length):
            
            if nums[i]>=0:
                all_negative = False
                break
            negative_max = max(negative_max, nums[i])

        if all_positive:
            return sum(nums)
        
        if all_negative:
            return negative_max

        runsum = 0
        ans = 0
        for i in range(length):
            ele = nums[i]
            runsum+=ele

            ans = max(runsum, ans)

            if runsum < 0:
                runsum = 0
                continue

        return ans
    


x = Solution()
y = x.maxSubArray([-1])
print(y)        


