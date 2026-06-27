# Last updated: 6/26/2026, 7:16:40 PM
1from collections import defaultdict
2
3class Solution:
4    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
5        itin = defaultdict(list)
6        result = []
7
8        for depart, land in sorted(tickets, reverse=True):
9            itin[depart].append(land)
10        
11        def dfs(flight):
12            
13            while itin[flight]:
14                nextflight = itin[flight].pop()
15                dfs(nextflight)
16            result.append(flight)
17        
18        dfs("JFK")
19        return result[::-1]