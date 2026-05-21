# Last updated: 5/21/2026, 11:31:31 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        
4        cleaned_s = ""
5
6        for c in s:
7            if c.isalnum():
8                c = c.lower()
9                cleaned_s += c
10
11        l, r = 0, len(cleaned_s)-1
12        while l < r:
13            if cleaned_s[l] != cleaned_s[r]:
14                return False
15
16            l += 1
17            r -= 1
18
19        return True