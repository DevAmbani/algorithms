# Last updated: 5/30/2026, 7:47:32 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        check_len = len(needle)
4
5        for i in range(len(haystack)):
6            if haystack[i:i+check_len] == needle:
7                return i
8        
9        return -1
10                