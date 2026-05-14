# Last updated: 5/13/2026, 11:04:19 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5
6        counts = defaultdict(int)
7        countt = defaultdict(int)
8
9        for i in range(len(s)):
10            counts[s[i]] += 1
11            countt[t[i]] += 1
12        
13        if counts == countt:
14            return True
15        else:
16            return False
17            