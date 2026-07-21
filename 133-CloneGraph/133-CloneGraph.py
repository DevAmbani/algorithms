# Last updated: 7/21/2026, 5:32:33 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        longest = ""
4
5        def expand(l, r):
6            while l >= 0 and r < len(s) and s[l] == s[r]:
7                l -= 1
8                r+= 1
9            
10            return s[l+1:r]
11        
12        for i in range(len(s)):
13            even = expand(i, i)
14            odd = expand(i, i+1)
15
16            if len(even) > len(longest):
17                longest = even
18            if len(odd) > len(longest):
19                longest = odd
20        
21        return longest
22
23