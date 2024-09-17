"""
Problem Description
You're given a read-only array of N integers. 
Find out if any integer occurs more than N/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Note: Read-only array means that the input array should not be modified in the process of solving the problem



Problem Constraints
1 <= N <= 7*105
1 <= A[i] <= 109


Input Format
The only argument is an integer array A.


Output Format
Return an integer.


Example Input
Input 1:
[1 2 3 1 1]
Input 2:
[1 2 3]


Example Output
Output 1:
1
Output 2:
-1


Example Explanation
Explanation 1:
1 occurs 3 times which is more than 5/3 times.
Explanation 2:
No element occurs more than 3 / 3 = 1 times in the array.
"""

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

"""




from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        candidate_a =  -1
        candidate_b = -1
        votes_a = 0
        votes_b = 0

        ans = []

        for i in range(n):
            
            if votes_a == 0 and nums[i] != candidate_b:
                votes_a +=1
                candidate_a = nums[i]
            elif votes_b == 0 and nums[i] != candidate_a:
                votes_b +=1
                candidate_b = nums[i]
            else:
                if nums[i] == candidate_a:
                    votes_a+=1
                elif nums[i] == candidate_b:
                    votes_b+=1
                else:
                    votes_a -= 1
                    votes_b -= 1

        freq_a = 0
        freq_b = 0

        for i in range(n):
            if nums[i] == candidate_a:
                freq_a += 1

            if nums[i] == candidate_b:
                freq_b += 1
        
        if freq_a > (n//3):
           ans.append(candidate_a)
        
        if candidate_b != candidate_a and  freq_b > (n//3):
            ans.append(candidate_b)
        
        return ans

s = Solution()
p = s.majorityElement([1,1,2,3,4,1,1,5,6,7,1,1,8,9,10,1,11,12,13,14])  
print(p)     
                