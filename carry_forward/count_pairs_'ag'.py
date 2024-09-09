"""
Problem : Count Pairs 'ag'
Comment
Given a character array ch[N] of size N, We have to calculate the number of pairs of indices i, j where i<j && ch[i] == 'a' && ch[j] == 'g'

Constraints
1 <= N <= 10^5
'a' <= ch[i] <= 'z'
Example
Input: ch[8] = {b, a, a, g, d, c, a, g}
Output: 5

Example Explanation:
Let us write an index of every element of an array

0	1	2	3	4	5	6	7
b	a	a	g	d	c	a	g
Pairs(i, j) where ch[i]='a' and ch[j]='g' and i<j are:

(1,3), (2,3), (1,7), (2,7), (6,7)

So there are total 5 pairs.
"""

char_arr = ['a', 'g', 'b', 'g', 'a', 'a', 'c', 'e', 'g']


g_count = 0
count = 0

for i in range(len(char_arr)-1, -1, -1):
   
    if char_arr[i]=='g':
      g_count+=1
    
    if char_arr[i]== 'a':
       count+=g_count

print(count)