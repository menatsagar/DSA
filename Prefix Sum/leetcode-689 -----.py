#https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/

"""
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)
"""
import math

class Solution(object):
    # def maxSumOfThreeSubarrays(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     # created prefix_sum array
    #     prefix_sum = []
    #     prefix_sum[0] = nums[0]
    #     ans = []
    #     for i in range(1, len(nums)):
    #         prefix_sum[i] = nums[i] + prefix_sum[i-1]

    #     length = len(nums)

    #     if length<=3:
    #         return [0,1,2]
    #     elif length ==6 and k==2:
    #         return [0,2,4]
    #     else:   

    #         initial_sum = 0
    #         for i in range(k):
    #             initial_sum+=nums[i]


    def maxSumOfThreeSubarrays(self, nums, k: int):
            # create an array to store the sums of each subarray
            sums = [0] * (len(nums) - k + 1)
            # calculate the sums of each subarray and store them in the array
            for i in range(len(nums) - k + 1):
                for j in range(k):
                    sums[i] += nums[i + j]
            # initialize the max sum to be the sum of the first three subarrays
            max_sum = sums[0] + sums[1] + sums[2]
            # initialize the indices of the max sum subarrays to be the indices of the first three subarrays
            max_sum_indices = [0, 1, 2]
            # iterate through the array of sums
            for i in range(3, len(sums)):
                # iterate through the indices of the previous max sum subarrays
                for j in max_sum_indices:
                    # if the current sum is greater than the previous max sum, update the max sum and its indices
                    if sums[i] > sums[j]:
                        max_sum = max_sum - sums[j] + sums[i]
                        max_sum_indices[j] = i
                        break
            # return the indices of the max sum subarrays
            return max_sum_indices
    
