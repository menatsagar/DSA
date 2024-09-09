"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

# NOTE: Brute-Forces

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        index = 0
        for num in nums:
            
            if (num == k):
                count+=1
            local_sum = num
           
            for j in range(index+1, len(nums)):
                
                local_sum+= nums[j]
                if(local_sum==k):
                    count+=1
            index+=1

        return count
    



#optimized

class Solution(object):

    def optsubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        index = 0
        runsum = 0
        d= { 0: 1}
        for num in nums:
            
            runsum+=num

            diff = runsum-k
            if diff in d:
                 
                 count+= d[diff]

            if runsum not in d:
                 d[runsum] = 0
            d[runsum] += 1
            
            index+=1

        return count

p  = Solution()
print(p.optsubarraySum([1,2,3,4,5,6,7], 11))