# Last updated: 5/28/2026, 4:23:06 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        count = defaultdict(int)
4        l = 0
5        longest = 0
6        freq = 0
7
8        for r in range(len(s)):
9            count[s[r]] += 1
10            freq = max(freq, count[s[r]])
11
12            while (r-l+1)-freq > k:
13                count[s[l]] -= 1
14                l += 1
15
16            longest = max(longest, (r-l+1))
17        
18        return longest