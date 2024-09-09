# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/  - LeetCode 121
"""
Problem Description
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Return the maximum possible profit.



Problem Constraints
0 <= A.size() <= 700000
1 <= A[i] <= 107



Input Format
The first and the only argument is an array of integers, A.


Output Format
Return an integer, representing the maximum possible profit.


Example Input
Input 1:
A = [1, 2]
Input 2:

A = [1, 4, 5, 2, 4]


Example Output
Output 1:
1
Output 2:

4


Example Explanation
Explanation 1:
Buy the stock on day 0, and sell it on day 1.
Explanation 2:

Buy the stock on day 0, and sell it on day 2.
"""

import math

def get_max(a, b):
    if a>b:
        return a
    return b

A = [1,2]
least_buy_price = math.inf
max_profit = 0
for i in range(len(A)):
    if A[i] < least_buy_price:
        least_buy_price = A[i]

    max_profit = get_max(max_profit, A[i]-least_buy_price) 

print(max_profit)
