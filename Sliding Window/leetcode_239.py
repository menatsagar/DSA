 #https://leetcode.com/problems/sliding-window-maximum/description/


# TODO: This could further optimized using Deque - NOT SOLVED USING DEQUE AND NOT SUBMITTED TO LEETCODE
"""

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        
        l = len(nums)
        ans = [0] * (l-k+1)
        max_index = 0

        for i in range(1,k):
           if nums[i]> nums[max_index]:
               max_index = i
        ans[0] = max_index

        for i in range(1, l-k+1):

            new_element_index = i+k-1
            prev_element_index = i-1
            if prev_element_index != max_index:
                if nums[new_element_index] > nums[max_index]:
                    max_index = new_element_index
            else:
                max_index = i
                for j in range(i+1, i+k):
                    if nums[j] > nums[max_index]:
                        max_index = j
            ans[i] = max_index

        for i in range(len(ans)):
            ans[i] = nums[ans[i]]

        return ans
    

s = Solution()
ans = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print(ans)


 