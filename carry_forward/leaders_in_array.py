"""
Problem : Leaders in Array
Comment
Given an array ar[N], you have to find a number of leaders in the array.

Leader: An element ar[i] is said to be a leader if it is greater than the maximum element of all elements present on the left of it i.e [0,i-1]

Note:
ar[0] is already considered a leader.

Constraints
1 <= N <= 10^5
1 <= ar[i] <= 10^9
Example
Input: ar[8] = {3, 2, 4, 5, 2, 7, -1, 15}
Output: 5

Example Explanation:

Index	                                                    0	1	2	3	4	5	6	7
Elements                                               	    3	2	4	5	2	7	-1	15
Maximum of elements present at left of current element	-	3	3	4	5	5	7	7
Leader	                                                    yes	x	yes	yes	x	yes	x	yes
"""
arr = [3, 2, 4, 5, 2, 7, -1, 15]

max_on_left = arr[0]
count = 1

for i in range(1, len(arr)):
    if arr[i] > max_on_left :
        max_on_left = arr[i]
        count +=1

print(count)