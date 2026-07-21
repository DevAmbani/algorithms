# Last updated: 7/21/2026, 5:39:44 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        self.count = 0
4
5        def expand(l, r):
6            while l >= 0 and r < len(s) and s[l] == s[r]:
7                l -= 1
8                r += 1
9                self.count += 1
10        
11        for i in range(len(s)):
12            even = expand(i, i)
13            odd = expand(i, i+1)
14
15        return self.count