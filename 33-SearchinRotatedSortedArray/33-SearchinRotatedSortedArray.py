# Last updated: 5/27/2026, 7:49:47 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        longest = 0
4        window = ""
5        for c in s:
6            if c not in window:
7                window += c
8                length = len(window)
9                longest = max(longest, length)
10            else:
11                while c in window:
12                    window = window[1:]
13                window += c
14
15        return longest