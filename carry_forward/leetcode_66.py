#https://leetcode.com/problems/plus-one/description/
"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.


Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].


Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].


Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""





class Solution:

    def plusOne(self, digits):

        n = len(digits)-1

        for index in range(n, -1, -1):
            digits[index] += 1

            if digits[index] % 10 != 0:
                return digits
            
            digits[index] %=10

        return [1] + digits


s = Solution()
ans1  = s.plusOne([9,9,9])
ans2 = s.plusOne([9,1,9])
ans3  = s.plusOne([1,2,9])
ans4  = s.plusOne([9])
ans5  = s.plusOne([1,2,9])
ans6  = s.plusOne([9])
ans7  = s.plusOne([3,4,5])
ans8  = s.plusOne([6,8,9])
ans9  = s.plusOne([1])
ans0  = s.plusOne([3,9,8])


print(ans0, ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9)



# pythonic solution

class Solution(object):
    def plusOne(self, digits):
        val = int(''.join(map(str, digits))) + 1
        return [int(i) for i in str(val)]