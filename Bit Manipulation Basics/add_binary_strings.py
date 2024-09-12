# Leetcode 67
"""
Problem Description
Given two binary strings A and B. Return their sum (also a binary string).


Problem Constraints
1 <= length of A <= 105

1 <= length of B <= 105

A and B are binary strings



Input Format
The two argument A and B are binary strings.



Output Format
Return a binary string denoting the sum of A and B



Example Input
Input 1:
A = "100"
B = "11"
Input 2:
A = "110"
B = "10"


Example Output
Output 1:
"111"
Output 2:
"1000"


Example Explanation
For Input 1:
The sum of 100 and 11 is 111.
For Input 2:
 
The sum of 110 and 10 is 1000.
"""

class Solution:

    def add_two_binary_strings(self,a,b):
        carry = 0
        ans = ""
        m = len(a)-1
        n = len(b)-1
        
        while m>=0 or n>=0:
        
            d1 = d2 = 0

            if m>=0:
                d1 = int(a[m])
        
            if n>=0:
                d2 = int(b[n])

            

            d = (d1+d2+carry)%2

            carry = (d1+d2+carry)//2
            
            ans = str(d)+ans 
            m-=1
            n-=1
            if (m<0 and n<0 and carry>0):
                ans = str(carry)+ans
        return ans
    

# A = "100"
# B = "11"

A = "110"
B = "10"

s = Solution()
p = s.add_two_binary_strings(A, B)
print(p)