# Last updated: 5/29/2026, 6:58:50 PM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        count = defaultdict(int)
4        for c in t:
5            count[c] += 1
6
7        new = defaultdict(int)
8        l = 0
9        ans = ""
10        min_len = float("inf")
11
12        for r in range(len(s)):
13            new[s[r]] += 1
14
15            while all(new[c] >= count[c] for c in count):
16                if r - l + 1 < min_len:
17                    min_len = r - l + 1
18                    ans = s[l:r+1]
19                new[s[l]] -= 1
20                l += 1
21
22        return ans