
"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

    

s = "cbaebabacd" 
p = "abc"



class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        
        freq_array_s = [0]*26
        freq_array_p = [0]*26

        n = len(s)
        P = len(p)
        ans = []
        
        if P>n:
            return ans

        for i in range(len(p)):
            freq_array_p[ord(p[i])-97]+=1
        
        for j in range(P):
            freq_array_s[ord(s[j])-97]+=1
        
        if freq_array_p == freq_array_s:
            ans.append(0)
        
        for k in range(1, n-P+1):
            next_ele = s[k+P-1]
            prev_ele = s[k-1]

            freq_array_s[ord(prev_ele)-97] -= 1
            freq_array_s[ord(next_ele)-97] += 1
        
            flag = self.is_both_freq_same(freq_array_s, freq_array_p)
            if flag:
                ans.append(k)
        
        return ans
  
    
    def is_both_freq_same(self, s, p):

        for i in range(26):
            
            if s[i] != p[i]:
                return False
        return True
  

sol = Solution()
obj =sol.findAnagrams(s,p)
print(obj)